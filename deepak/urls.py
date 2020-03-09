from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [

    path('', include('dgbook.urls', namespace='dgbook')),
    path('admin/', admin.site.urls),
]