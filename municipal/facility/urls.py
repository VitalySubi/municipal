from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'municipal/', views.municipal, name='municipal'),
    path('infosys', views.infoSys, name='infoSys'),
    path('diagnostics', views.diagnostics, name='diagnostics'),
    path('department', views.tvsp, name='tvsp'),
    path('networkstructure', views.tvspNetworkStructure, name='tvspNetworkStructure'),
    path('localnetwork', views.localNetwork, name='localNetwork'),
    path('protectednetwork', views.protectedNetwork, name='protectedNetwork'),
    path('internetaccess', views.internetAccess, name='internetAccess'),
    path('computer', views.computer, name='computer'),
    path('sysbody', views.sysBody, name='sysBody'),
    path('display', views.display, name='display'),
    path('mouse', views.mouse, name='mouse'),
    path('keyboard', views.keyboard, name='keyboard'),
    path('software', views.software, name='software'),
    path('', views.index, name='index'),
]