from django.shortcuts import render
from .models import pageModel

# Create your views here.
def indexView(request):
    context_obj = {
        'pages': pageModel.objects.all()
    }

    return render(request, 'index.html', context=context_obj)

def waybackView(request):
    return render(request, 'wayback.html')

def timebackView(request):
    return render(request, 'timemachine.html')

def prView(request):
    return render(request, 'pr.html')