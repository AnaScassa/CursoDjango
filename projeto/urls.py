from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# HTTP REQUEST
def my_view(request):
    return HttpResponse('Olá mundo!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', my_view),
    path('recipes/', include('recipes.urls')),
]
