from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms.UserProfileForm import UserProfileForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def dashboard(request):
    googleUserId = request.user.id
    if UserProfile.objects.filter(user_no=googleUserId):

        print(request.session.items())
        return render(request, 'main/dashboard.html')
    else:
        return redirect('create_user_profile')


@login_required(login_url='/accounts/login/')
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            # Set user_no programmatically
            user_profile.user_no = request.user.id  # Replace with actual logic to determine user_no
            user_profile.save()
            return redirect('profile_success')  # Replace with your success URL
        else:
            print(form.errors)  # Debugging form errors
    else:
        form = UserProfileForm()

    return render(request, 'main/userdetails.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile_success(request):
    return render(request, 'main/dashboard.html')