from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='home page'),
    path('delete_items/<int:pk>/', views.delete_items, name='delete_items'),
    path('user/', views.register,name='register-view'),
    path('login/', auth_views.LoginView.as_view(template_name='task/login.html') ,name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='task/logout.html') ,name='logout'),  
    path('customer/<customer_id>', views.customer_view, name="customer"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
