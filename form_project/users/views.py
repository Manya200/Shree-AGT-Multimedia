from django.shortcuts import render , redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database
            messages.success(request, "Form submitted successfully!")  # Success message
            return redirect("home")  # Redirect to the form page after submission
        else:
            messages.error(request, "Please correct the errors below.")  # Error message
    else:
        form = UserForm()
    return render(request, "users/user_form.html", {"form": form})

def user_list(request):
    users = User.objects.all()
    return render(request,'users/user_list.html',{'users':users})


