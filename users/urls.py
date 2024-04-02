from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileUpdateView, ProfileView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login_page/', LoginView.as_view(), name='login_page'),
    path('logout_page/', LogoutView.as_view(), name='logout_page'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile_view/', ProfileView.as_view(), name='profile_view'),   
]



