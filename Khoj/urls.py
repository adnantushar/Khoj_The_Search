from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register('', SearchListViewSet, basename='searchlist')


urlpatterns = [
    path('signup/', SignUp, name="signup"),
    path('login/', LogIn, name="login"),
    path('logout/', LogOut, name="logout"),
    path('',Home, name="home"),
    path('searchlist/',SearchList,name='searchlist'),
    path('api/', include((router.urls, 'khoj')))
]