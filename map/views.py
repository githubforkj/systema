from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel, latlon, heat_read, heat_orange
from .example import map

#class IndexView(TemplateView):
        #template_name="index.html"
def index(request):
    data = latlon.objects.all()
    data1= heat_read.objects.all()
    data2= heat_orange.objects.all()
    params = {
            'data': data,
            'data1': data1,
            'data2': data2,
            }
    return render(request, 'index.html', params)

def ajax_number(request):
    lat = float(request.POST.get('lat'))
    lon = float(request.POST.get('lon'))
    d = {
        'lat': lat,
        'lon': lon,
    }
    return JsonResponse(d)

class ListClass(ListView):
        template_name="list.html"
        model = PostModel

class FormClass(CreateView):
        template_name = 'form.html'
        model = PostModel
        fields = ('title','memo')
        success_url = reverse_lazy('list')

from .scripts  import test1

def test(request):
    if request.method == 'POST':
        a = test1().print_word()
        if 'button_1' in request.POST:
            test1().print_word()
        lat = request.POST['lat']
        lon = request.POST['lon']
        b = list((lat,lon))
        # b = test1().map(float(lat),float(lon))
        return HttpResponse('<h1>Page was found</h1> %s' % b)
