from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name='logout'),
    path('signup/', signup, name='signup'),
    path('AD/', AD.as_view(), name='advertisment'),
    path('ADForm/', CreateAD, name='add_AD'),
    path('success', success, name = 'success')
]