from django.contrib import admin
from django.urls import path,include
from users import views as users_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myfood/',include('myfood.urls')),
    path('register',users_view.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path('profile/',users_view.profile,name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

