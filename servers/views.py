from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Server


def index(request):
    server_list = Server.objects.order_by('-created')
    template = loader.get_template('servers/index.html')
    context = {
        'server_list': server_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, hostname):
    server = get_object_or_404(Server, hostname=hostname)
    return render(request, 'servers/detail.html', {'server': server})
