from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="Home"),
    path('login/', views.logincheck, name="login"),
    path('logout/', views.logoutcheck, name="login"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



