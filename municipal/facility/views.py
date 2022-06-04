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
    return HttpResponse("Страница информационной системы")


def diagnostics(request):
    return HttpResponse("Страница диагностического оборудования")


def tvsp(request):
    return HttpResponse("Страница ТВСП")


def tvspNetworkStructure(request):
    return HttpResponse("Страница сетевой инфраструктуры ТВСП")


def localNetwork(request):
    return HttpResponse("Страница ЛВС")


def protectedNetwork(request):
    return HttpResponse("Страница защищённой СПД")


def internetAccess(request):
    return HttpResponse("Страница доступа в Интернет")


def computer(request):
    return HttpResponse("Страница АРМ")


def sysBody(request):
    return HttpResponse("Страница системного блока")


def display(request):
    return HttpResponse("Страница монитора")


def mouse(request):
    return HttpResponse("Страница мыши")


def keyboard(request):
    return HttpResponse("Страница клавиатуры")


def software(request):
    return HttpResponse("Страница ПО")
