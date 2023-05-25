from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from UserModule.models import User, Company, Project, Task


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
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_admin=True)
        elif role == 'is_owner':
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_owner=True)
        elif role == 'is_manager':
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_manager=True)
        elif role == 'is_supervisor':
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_supervisor=True)
        elif role == 'is_assistant':
            user = User.objects.create_user(
                username=request.POST['name'], email=request.POST['email'], password=request.POST['password'], is_assistant=True)
        user.save()

    people = User.objects.all()
    userInfo = []

    for i in people:
        if i.is_admin == True:
            userInfo.append(
                {'name': i.username, 'role': "Admin", 'email': i.email})
        elif i.is_owner == True:
            userInfo.append(
                {'name': i.username, 'role': "Owner", 'email': i.email})
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


@login_required
def Companies(request):
    if (request.method == 'POST'):
        user = request.user
        name = request.POST['name']
        dbaName = request.POST['dbaName']
        address = request.POST['address']
        branch = request.POST['branch']
        number = request.POST['phone']
        website = request.POST['website']
        fax = request.POST['fax']
        email = request.POST['email']

        data = Company(user=user, name=name, dbaName=dbaName, address=address,
                       branch=branch, number=number, website=website, fax=fax, email=email)
        data.save()
        return HttpResponseRedirect('/Companies')

    else:
        print(request.user.is_owner)
        print(request.user.is_manager)
        data = Company.objects.all()
        return render(request, 'CompanyManagement/DashBoard/Companies.html', {'data': data})


@login_required
def CompaniesEdit(request, pk):
    if (request.method == 'POST'):
        user = request.user
        name = request.POST['name']
        dbaName = request.POST['dbaName']
        address = request.POST['address']
        branch = request.POST['branch']
        number = request.POST['phone']
        website = request.POST['website']
        fax = request.POST['fax']
        email = request.POST['email']

        data = Company.objects.filter(id=pk).update(user=user, name=name, dbaName=dbaName, address=address,
                                                    branch=branch, number=number, website=website, fax=fax, email=email)
        # data.save()
        return HttpResponseRedirect('/Companies')
    else:
        data = Company.objects.get(pk=pk)
        return render(request, 'CompanyManagement/DashBoard/CompaniesEdit.html', {'data': data})


@login_required
def Projects(request):
    if (request.method == 'POST'):
        user = request.user
        company = request.POST['company']
        company = Company.objects.get(name=company)
        name = request.POST['name']
        description = request.POST['description']
        manager = request.POST['manager']
        supervisor = request.POST['supervisor']
        assistants = request.POST['assistants']

        data = Project(user=user, company=company, name=name, description=description,
                       manager=manager, supervisor=supervisor, assistants=assistants)
        data.save()
        return HttpResponseRedirect('/Projects')
    else:
        company = Company.objects.all()
        project = Project.objects.all()
        return render(request, 'CompanyManagement/DashBoard/Projects.html', {'company': company, 'project':  project})


@login_required
def ProjectsEdit(request, pk):
    if (request.method == 'POST'):
        user = request.user
        company = request.POST['company']
        company = Company.objects.get(name=company)
        name = request.POST['name']
        description = request.POST['description']
        manager = request.POST['manager']
        supervisor = request.POST['supervisor']
        assistants = request.POST['assistants']

        data = Project.objects.filter(id=pk).update(user=user, company=company, name=name, description=description,
                                                    manager=manager, supervisor=supervisor, assistants=assistants)
        # data.save()
        return HttpResponseRedirect('/Projects')
    else:
        company = Company.objects.all()
        project = Project.objects.get(pk=pk)
        return render(request, 'CompanyManagement/DashBoard/ProjectsEdit.html', {'company': company, 'project':  project})


@login_required
def Tasks(request):
    if (request.method == 'POST'):
        user = request.user
        company = request.POST['company']
        company = Company.objects.get(name=company)
        project = request.POST['project']
        project = Project.objects.get(name=project)
        name = request.POST['name']
        description = request.POST['description']
        manager = request.POST['manager']
        supervisor = request.POST['supervisor']
        assistants = request.POST['assistants']

        data = Task(user=user, company=company,
                    project=project, name=name, description=description,
                    manager=manager, supervisor=supervisor, assistants=assistants)
        data.save()
        return HttpResponseRedirect('/Tasks')
    else:
        company = Company.objects.all()
        project = Project.objects.all()
        task = Task.objects.all()
        return render(request, 'CompanyManagement/DashBoard/Tasks.html', {'company': company, 'project':  project, 'task': task})


@login_required
def TasksEdit(request, pk):
    if (request.method == 'POST'):
        user = request.user
        company = request.POST['company']
        company = Company.objects.get(name=company)
        project = request.POST['project']
        project = Project.objects.get(name=project)
        name = request.POST['name']
        description = request.POST['description']
        manager = request.POST['manager']
        supervisor = request.POST['supervisor']
        assistants = request.POST['assistants']

        data = Task.objects.filter(id=pk).update(user=user, company=company,
                                                 project=project, name=name, description=description,
                                                 manager=manager, supervisor=supervisor, assistants=assistants)
        # data.save()
        return HttpResponseRedirect('/Tasks')
    else:
        company = Company.objects.all()
        project = Project.objects.all()
        task = Task.objects.get(id=pk)
        return render(request, 'CompanyManagement/DashBoard/TasksEdit.html', {'company': company, 'project':  project, 'task': task})
