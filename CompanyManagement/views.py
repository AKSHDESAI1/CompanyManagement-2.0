from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from UserModule.models import User


class Login(LoginView):
    template_name = 'CompanyManagement/AuthModule/Authentication/login.html'


class Logout(LogoutView):
    template_name = 'CompanyManagement/AuthModule/Authentication/logout.html'


class ChangePassword(PasswordChangeView):
    template_name = 'CompanyManagement/AuthModule/ChangePassword/ChangePassword.html'
    success_url = '/change-password-Done/'


class ChangePasswordDone(PasswordChangeDoneView):
    template_name = 'CompanyManagement/AuthModule/ChangePassword/ChangePasswordDone.html'


class ResetPassword(PasswordResetView):
    template_name = 'CompanyManagement/AuthModule/ForgotPassword/ResetPassword.html'
    success_url = '/reset-Password-Done/'


class ResetPasswordDone(PasswordResetDoneView):
    template_name = 'CompanyManagement/AuthModule/ForgotPassword/ResetPasswordDone.html'
    success_url = '/reset-Password-Done/'


class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = 'CompanyManagement/AuthModule/ForgotPassword/ResetPasswordConfirm.html'
    success_url = '/reset/done/'


class ResetPasswordComplete(PasswordResetCompleteView):
    template_name = 'CompanyManagement/AuthModule/ForgotPassword/ResetPasswordComplete.html'


@login_required
def People(request):
    if request.method == 'POST':
        a = request.POST
        role = request.POST['role']
        print('role', role)
        if role == 'is_admin':
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_admin = True)
        elif role == 'is_manager':
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_manager = True)
        elif role == 'is_supervisor':
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_supervisor = True)
        elif role == 'is_assistant':
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_assistant = True)
        user.save()

    people = User.objects.all()
    userInfo = []

    for i in people:
        if i.is_admin == True:
            userInfo.append(
                {'name': i.username, 'role': "Admin", 'email': i.email})
        elif i.is_manager == True:
            userInfo.append(
                {'name': i.username, 'role': "Manager", 'email': i.email})
        elif i.is_supervisor == True:
            userInfo.append(
                {'name': i.username, 'role': "Supervisor", 'email': i.email})
        elif i.is_assistant == True:
            userInfo.append(
                {'name': i.username, 'role': "Assistant", 'email': i.email})
        else:
            userInfo.append(
                {'name': i.username, 'role': "Not Found", 'email': i.email})

    return render(request, 'CompanyManagement/DashBoard/People.html', {'userInfo': userInfo})
