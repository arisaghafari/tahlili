from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, signup, AD

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.LogoutView, {'next_page': 'login'}, name='logout'),
    path('signup/', signup, name='signup'),
    path('AD/', AD.as_view(), name='advertisment'),
]