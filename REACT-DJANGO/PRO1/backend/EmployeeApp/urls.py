from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department', views.departmentApi, name='departmentApi'),
    path('department/<int:id>', views.departmentApi, name='departmentApi'),
    path('employee', views.employeeApi, name='employeeApi'),
    path('employee/<int:id>', views.employeeApi, name='employeeApi'),
    path('employee/saveFile', views.saveFile, name='saveFile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)