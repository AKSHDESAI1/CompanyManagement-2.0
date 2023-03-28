
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
    # path('People/', login_required(TemplateView.as_view(
    #     template_name='CompanyManagement/DashBoard/People.html')), name='People'),
    path('People/', views.People, name='People'),
    path('Companies/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/Companies.html')), name='Companies'),
    path('Projects/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/Projects.html')), name='Projects'),
    path('Tasks/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/Tasks.html')), name='Tasks'),
    path('Messages/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/Messages.html')), name='Messages'),
    path('Activity_Overview/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/Activity_Overview.html')), name='Activity_Overview'),
    path('Profile/', login_required(TemplateView.as_view(
        template_name='CompanyManagement/DashBoard/Profile.html')), name='Profile'),


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
