from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.<app_name>.api.v1.urls')),
]
