from rest_auth.registration.views import VerifyEmailView

from django.conf.urls import url

from .api import views

urlpatterns = [
    url('register/', views.UserRegisterView.as_view(), name='register'),
    url('confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email'),
]
