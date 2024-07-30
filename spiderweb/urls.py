# main urls.py
from django.contrib import admin
from django.urls import path, include
from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('userauth/', include('userauth.urls')),
    path('blog/', include('blog.urls')),
    path('toolkit/', include('tool_kit.urls')),
]
