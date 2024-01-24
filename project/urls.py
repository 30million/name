
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    # admin path
    path('admin/', admin.site.urls),
    # include all path in app application
    path('' , include('app.urls')),
]
