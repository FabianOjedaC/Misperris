from django.conf.urls import url
from social_django.urls import urlpatterns, app_name
from django.urls import path,include
from . import views
from django.conf.urls import include
from rest_framework import routers
from Sistema.quickstart import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)

router.register(r'groups', views.GroupViewSet)

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^registro/$',views.registroPersona,name="registro"),
    url(r'^login/$',views.ingreso,name="login"),
    url(r'^olvido/$',views.olvido,name="olvido"),
    url(r'^restablecer/$',views.restablecer,name="restablecer"),
    url(r'^registroPerro/$', views.registroPerro, name='registroPerro'),
    url(r'^registroAdmin/$', views.registroAdmin, name='registroAdmin'),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^Adoptar/$',views.registroPerro,name="adoptaPerro"),
    url('', include('social_django.urls', namespace='social')),
    url('accounts/', include('allauth.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'