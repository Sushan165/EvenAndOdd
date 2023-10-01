from django.contrib import admin
from django.urls import path
from eoapp.views import ulogin, usignup,uhome,usnp,ulogout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ulogin",ulogin,name="ulogin"),
    path("usignup",usignup,name="usignup"),
    path("",uhome,name="uhome"),
    path("ulogout",ulogout,name="ulogout"),
]
