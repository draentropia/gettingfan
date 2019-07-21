from django.shortcuts import render
from django.shortcuts import render_to_response, render
from . import arduino_control

# Create your views here.
def index(request):
    if (request.GET.get('switch_on')):
        arduino_control.send_order('1')

    if (request.GET.get('switch_off')):
        arduino_control.send_order('0')
    return render(request, 'index.html')