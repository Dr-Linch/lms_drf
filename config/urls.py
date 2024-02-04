from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lms_app.urls', namespace='lms')),
    path('user/', include('users.urls', namespace='users')),
    path('payments/', include('payments.urls', namespace='payments')),
]