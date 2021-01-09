from django.shortcuts import render, HttpResponseRedirect
from .forms import ChildRegistration
from .models import Registration

# Create your views here.

#THIS FUNCTION WILL ADD NEW ITEMS AND SHOW ITEMS
def add(request):
    if request.method == 'POST':
        my_form = ChildRegistration(request.POST)
        if my_form.is_valid():
            c_name = my_form.cleaned_data['child_name']
            c_age = my_form.cleaned_data['child_age']
            c_dob = my_form.cleaned_data['child_dob']
            c_gender = my_form.cleaned_data['child_gender']
            m_name = my_form.cleaned_data['mother_name']
            m_age = my_form.cleaned_data['mother_age']
            reg = Registration(child_name=c_name, child_age=c_age, child_dob=c_dob, child_gender=c_gender, mother_name=m_name, mother_age=m_age)
            reg.save()
            my_form = ChildRegistration()
    else:
        my_form = ChildRegistration()
    show = Registration.objects.all()
    return render(request, 'registration/register.html', {'form': my_form})

#THIS REPRESENTS THE VIEWING FUNCTION - WITH THIS YOU CAN VIEW RECORDS FROM THE DATABASE
def view_data(request):
    show = Registration.objects.all()
    return render(request, 'registration/view.html', {'showrecords': show})


#THIS IS THE FUNCTION FOR EDITING OR UPDATING DATA
def update_data(request, id):
    if request.method == 'POST':
        update_user = Registration.objects.get(pk=id)
        fom = ChildRegistration(request.POST, instance=update_user)
        if fom.is_valid():
            fom.save()
    else:
        update_user = Registration.objects.get(pk=id)
        fom = ChildRegistration(instance=update_user)
    return render(request,'registration/update.html', {'form': fom})


# DELETE FUNCTION
def delete_data(request, id):
    if request.method == "POST":
        del_user = Registration.objects.get(pk=id)
        del_user.delete()
        return HttpResponseRedirect('/view')
