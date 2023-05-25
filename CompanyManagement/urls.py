
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Authentication related path
    path('admin/', admin.site.urls),
    path('login/', views.Login.as_view(), name='login'),
    path('profile/', TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/profile.html'), name='profile'),

    # Login Required for Access Home-page
    path('', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/home.html')), name='home'),
    path('People/', views.People, name='People'),
    path('Companies/', views.Companies, name='Companies'),
    path('Companies/update/<int:pk>', views.CompaniesEdit, name='CompaniesEdit'),
    path('Projects/', views.Projects, name='Projects'),
    path('Projects/update/<int:pk>', views.ProjectsEdit, name='ProjectsEdit'),
    path('Tasks/', views.Tasks, name='Tasks'),
    path('Tasks/update/<int:pk>', views.TasksEdit, name='TasksEdit'),
    path('Messages/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/Messages.html')), name='Messages'),
    path('Activity_Overview/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/Activity_Overview.html')), name='Activity_Overview'),
    path('Profile/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/profile.html')), name='Profile'),


    path('logout/', views.Logout.as_view(), name='logout'),


    # Change-Password for Authenticated Users
    path('change-password/', views.ChangePassword.as_view(), name='changePassword'),
    path('change-password-Done/', views.ChangePasswordDone.as_view(),
         name='changePasswordDone'),

    # Forgot-Password for Un-Authenticated Users
    path('reset-Password/', views.ResetPassword.as_view(),
         name='resetPassword'),
    path('reset-Password-Done/', views.ResetPasswordDone.as_view(),
         name='resetPasswordDone'),
    path('reset/<slug:uidb64>/<slug:token>/', views.ResetPasswordConfirm.as_view(),
         name='password_reset_confirm'),
    path(
        "reset/done/",
        views.ResetPasswordComplete.as_view(),
        name="password_reset_complete",
    ),

]
