from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'municipal', views.municipalView, name='municipal'),
    path('infosys', views.infoSysView, name='infoSys'),
    path('diagnostics', views.diagnosticsView, name='diagnostics'),
    path('department', views.tvspView, name='tvsp'),
    path('networkstructure', views.tvspNetworkStructureView, name='tvspNetworkStructure'),
    path('localnetwork', views.localNetworkView, name='localNetwork'),
    path('protectednetwork', views.protectedNetworkView, name='protectedNetwork'),
    path('internetaccess', views.internetAccessView, name='internetAccess'),
    path('computer', views.computerView, name='computer'),
    path('sysBlock', views.sysBlockView, name='sysBlock'),
    path('monitor', views.monitorView, name='monitor'),
    path('mouse', views.mouseView, name='mouse'),
    path('keyboard', views.keyboardView, name='keyboard'),
    path('software', views.softwareView, name='software'),
    path('', views.indexView, name='index'),
]