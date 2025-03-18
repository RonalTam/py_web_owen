from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def ao_view(request):
    return render(request, 'website/ao.html')
