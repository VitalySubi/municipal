from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from .models import Monitor

sideBarParams = {"main": {"collapsed": "collapsed", "expanded": "false", "show": ""},
                 "network": {"collapsed": "collapsed", "expanded": "false", "show": ""},
                 "facility": {"collapsed": "collapsed", "expanded": "false", "show": ""}}

itemsSelection = {"municipal": "",
                  "infoSys": "",
                  "diagnostics": "",
                  "tvsp": "",
                  "tvspNetworkStructure": "",
                  "localNetwork": "",
                  "protectedNetwork": "",
                  "internetAccess": "",
                  "computer": "",
                  "sysBlock": "",
                  "monitor": "",
                  "keyboard": "",
                  "mouse": "",
                  "software": ""}


def expandByKey(key):
    for i in sideBarParams.keys():
        sideBarParams[i]["collapsed"] = "collapsed"
        sideBarParams[i]["expanded"] = "false"
        sideBarParams[i]["show"] = ""

    sideBarParams[key]["collapsed"] = ""
    sideBarParams[key]["expanded"] = "true"
    sideBarParams[key]["show"] = "show"


def selectByKey(key):
    for i in itemsSelection.keys():
        itemsSelection[i] = ""

    itemsSelection[key] = "on-selected"


def indexView(request):
    #return HttpResponse("Главная")
    data = {"header": "Главная", "message": "Добро пожаловать!", "sideBarParams": sideBarParams}
    return render(request, "facility/index.html", context=data)


def municipalView(request):
    id = request.GET.get("municipalId")
    data = {"id": id}
    expandByKey("main")
    selectByKey("municipal")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse(f"Страница муниципального учреждения {id}")
    return render(request, "facility/municipal_page.html", context=data)


def infoSysView(request):
    expandByKey("main")
    selectByKey("infoSys")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница информационной системы")
    return render(request, "facility/infosys_page.html", context=data)


def diagnosticsView(request):
    expandByKey("main")
    selectByKey("diagnostics")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница диагностического оборудования")
    return render(request, "facility/diagnostics_page.html", context=data)


def tvspView(request):
    expandByKey("main")
    selectByKey("tvsp")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница ТВСП")
    return render(request, "facility/tvsp_page.html", context=data)


def tvspNetworkStructureView(request):
    expandByKey("network")
    selectByKey("tvspNetworkStructure")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница сетевой инфраструктуры ТВСП")
    return render(request, "facility/networkstructure_page.html", context=data)


def localNetworkView(request):
    expandByKey("network")
    selectByKey("localNetwork")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница ЛВС")
    return render(request, "facility/localnetwork_page.html", context=data)


def protectedNetworkView(request):
    expandByKey("network")
    selectByKey("protectedNetwork")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница защищённой СПД")
    return render(request, "facility/protectednetwork_page.html", context=data)


def internetAccessView(request):
    expandByKey("network")
    selectByKey("internetAccess")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница доступа в Интернет")
    return render(request, "facility/internetaccess_page.html", context=data)


def computerView(request):
    expandByKey("facility")
    selectByKey("computer")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница АРМ")
    return render(request, "facility/computer_page.html", context=data)


def sysBlockView(request):
    expandByKey("facility")
    selectByKey("sysBlock")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница системного блока")
    return render(request, "facility/sysblock_page.html", context=data)


def monitorView(request):
    monitors = Monitor.objects.all()
    print(monitors)
    expandByKey("facility")
    selectByKey("monitor")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection, "monitors": monitors}
    #return HttpResponse("Страница монитора")
    return render(request, "facility/monitor_page.html", context=data)


def monitorNewView(request):
    return render(request, "facility/add/monitor_new_page.html", context=None)


def monitorSaveView(request):
    newMonitor = Monitor(monmodel=request.POST.get("model"),
                         mondiag=request.POST.get("diag"),
                         moninv=request.POST.get("inv"),
                         mondate=datetime.strptime(request.POST.get("date"), "%d/%m/%Y"),
                         equid=None if request.POST.get("arm") == "" else request.POST.get("arm"))
    newMonitor.save()
    return redirect("/monitor", context=None)


def mouseView(request):
    expandByKey("facility")
    selectByKey("mouse")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница мыши")
    return render(request, "facility/mouse_page.html", context=data)


def keyboardView(request):
    expandByKey("facility")
    selectByKey("keyboard")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница клавиатуры")
    return render(request, "facility/keyboard_page.html", context=data)


def softwareView(request):
    expandByKey("facility")
    selectByKey("software")
    data = {"sideBarParams": sideBarParams, "itemsSelection": itemsSelection}
    #return HttpResponse("Страница ПО")
    return render(request, "facility/software_page.html", context=data)
