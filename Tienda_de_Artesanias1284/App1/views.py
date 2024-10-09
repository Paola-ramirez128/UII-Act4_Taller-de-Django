from django.shortcuts import render, get_object_or_404
from .models import Provedores, Sucursal
#from django.http import HttpResponse
# Create your views here.
def IndexView(request):
    "Esto es la Pagina Principal"

    objeto = Provedores.objects.all().order_by(-id)

    return render(request, "Index.html", {"objeto" : objeto})
def ProvedorView(request, id):
    provedor = get_object_or_404(Provedores, id=id)
    return render(request, "provedor.html", {"objeto" : provedor})


