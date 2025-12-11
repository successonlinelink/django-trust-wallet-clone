from django.shortcuts import render, redirect
from userauths import models as user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

from core import models as wallets_model
from accounts import forms as forms_model
# Create your views here.

# @login_required
def account(request):

    # account = request.user.profile    
    context = { 
        # "account": account
    }
    return render(request, 'accounts/account.html', context)

# Security
@login_required
def security(request):

    # account = request.user.profile    
    context = { 
        # "account": account
    }
    return render(request, 'accounts/security.html', context)

# Change Password
@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_new_password = request.POST.get("confirm_new_password")

        # Check if new and confirm passwords match
        if new_password != confirm_new_password:
            messages.error(request, "New password and confirmation do not match.")
            return redirect("account:change_password")

        # Check if old password is correct
        if check_password(old_password, request.user.password):
            request.user.set_password(new_password)
            request.user.save()

            # Keep the user logged in after changing password
            update_session_auth_hash(request, request.user)

            messages.success(request, "Password changed successfully.")
            return redirect("account:security")
        else:
            messages.error(request, "Old password is incorrect.")
            return redirect("account:change_password")

    return render(request, "accounts/change_password.html")


# Delete Account
@login_required
def delete_account(request):

    if request.method == 'POST':
        delete_account = user_model.User.objects.get(username=request.user)

        delete_account.delete()
        messages.success(request, "Account Deleted Successfully")
        return redirect('userauths:login')
    return render(request, 'accounts/delete_account.html')


# user profile
@login_required
def my_profile(request):
    
    profile = request.user.profile
    context = { 'profile': profile }
    return render(request, 'accounts/my-profile.html', context)

# update profile
@login_required
def verify_account(request):
    
    if request.method == "POST":
        form = forms_model.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('account:account_review')
    else:
        form = forms_model.ProfileUpdateForm() # instance=request.user.profile -> i dont want it to hold the user details in the inputs

    context = { 'form': form, }
    return render(request, 'accounts/verify_account.html', context)


# Account Review
@login_required
def account_review(request):
    
    context = { }

    return render(request, 'accounts/account_review.html', context)


# Privacy
@login_required
def privacy(request):
    
    context = { }

    return render(request, 'accounts/privacy.html', context)

# Authority
@login_required
def authority(request):
    
    context = { }

    return render(request, 'accounts/authority.html', context)





