
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from . import settings
from .views import base_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',include('books.urls', namespace='books')),
    path('users/',include('users.urls')),
    path('', base_page, name='base'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)