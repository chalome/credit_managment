
from django.contrib import admin
from django.urls import path,include
from credit.views import HomeView
from authentication.views import (
    UserCreationView,CustomLoginView,
    CustomLogoutView,userListView,
    UserUpdateView,UserDeleteView,PasswordChangeView)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeDoneView
from credit.views import(
  CreditCreateView,CreditUpdateView,
  CreditDetailView,CreditListView,
  CreditDeleteView,CreditViewSet
    )
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'credits',CreditViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('credit_home',HomeView.as_view(),name='credit_home'),
    path('',CustomLoginView.as_view(),name='login'),
    path('signup',UserCreationView.as_view(),name='signup'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
    path('user_list/',userListView.as_view(),name='user_list'),
    path('user_update/<int:user_id>',UserUpdateView.as_view(),name='user_update'),
    path('user_delete/<int:user_id>',UserDeleteView.as_view(),name='user_delete'),
    path('change_password',PasswordChangeView.as_view(),name='change_password'),
    path('change_password/done/',PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('credit_create',CreditCreateView.as_view(),name='credit_create'),
    path('credit_update/<int:credit_id>',CreditUpdateView.as_view(),name='credit_update'),
    path('credit_delete/<int:credit_id>',CreditDeleteView.as_view(),name='credit_delete'),
    path('credit_detail/<int:pk>',CreditDetailView.as_view(),name='credit_detail'),
    path('credit_list',CreditListView.as_view(),name='credit_list'),
    path('api/',include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)