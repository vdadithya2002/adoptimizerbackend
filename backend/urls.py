from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include, re_path
from django.views.generic import TemplateView

def api_home(request):
    return JsonResponse({"message": "Welcome to the Ad Optimization API!"})

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('ad_optimizer.urls')),  # API endpoints
    re_path(r'^.*$', TemplateView.as_view(template_name='build/index.html')),  # React app
]
