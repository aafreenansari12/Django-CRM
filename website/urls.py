# for web page 
# 3 step process
# actual temple, actual HTML page, create URL and view


from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    # path('/login',views.login_user, name='login'),
    # path('/logout',views.logout_user, name='logout'),
]
