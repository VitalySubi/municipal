from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Главная")
    data = {"header": "Главная", "message": "Добро пожаловать!"}
    return render(request, "facility/index.html", context=data)


def municipal(request):
    id = request.GET.get("municipalId")
    data = {"id": id}
    #return HttpResponse(f"Страница муниципального учреждения {id}")
    return render(request, "facility/municipal_page.html", context=data)


def infoSys(request):
    #return HttpResponse("Страница информационной системы")
    return render(request, "facility/infosys_page.html")


def diagnostics(request):
    #return HttpResponse("Страница диагностического оборудования")
    return render(request, "facility/diagnostics_page.html")


def tvsp(request):
    #return HttpResponse("Страница ТВСП")
    return render(request, "facility/tvsp_page.html")


def tvspNetworkStructure(request):
    #return HttpResponse("Страница сетевой инфраструктуры ТВСП")
    return render(request, "facility/municipal_page.html")


def localNetwork(request):
    #return HttpResponse("Страница ЛВС")
    return render(request, "facility/municipal_page.html")


def protectedNetwork(request):
    #return HttpResponse("Страница защищённой СПД")
    return render(request, "facility/municipal_page.html")


def internetAccess(request):
    #return HttpResponse("Страница доступа в Интернет")
    return render(request, "facility/municipal_page.html")


def computer(request):
    #return HttpResponse("Страница АРМ")
    return render(request, "facility/municipal_page.html")


def sysBody(request):
    #return HttpResponse("Страница системного блока")
    return render(request, "facility/municipal_page.html")


def display(request):
    #return HttpResponse("Страница монитора")
    return render(request, "facility/municipal_page.html")


def mouse(request):
    #return HttpResponse("Страница мыши")
    return render(request, "facility/municipal_page.html")


def keyboard(request):
    #return HttpResponse("Страница клавиатуры")
    return render(request, "facility/municipal_page.html")


def software(request):
    #return HttpResponse("Страница ПО")
    return render(request, "facility/municipal_page.html")
