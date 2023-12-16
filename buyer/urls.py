from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.user_signup,name="signup_page"),
    path('profile/',views.user_profie,name="profile_page"),
    path('profile/edit/',views.user_edit_profile,name="edit_profile_page"),
    path('login/',views.user_login,name="login_page"),
    path('logout/',views.user_logout,name="logout_page"),
]