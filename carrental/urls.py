
from django.contrib import admin
from django.urls import path

from carrent.views import home,process_page,in_page,up_page,index_page,home2,process2_page,success_page
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "car rental Admin"
admin.site.site_title = "car rental Admin Portal"
admin.site.index_title = "Welcome to car rental Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name='home'),
    path('process',process_page,name="process_page"),
    path('in',in_page,name="in_page"),
    path('index',index_page,name="index_page"),
    path('up',up_page,name="up_page"),
    path('home2',home2,name="home_page"),
    path('process2',process2_page,name="process2_page"),
    path('success/',success_page,name="success_page"),
    # path('success/', views.success_view, name='success'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)