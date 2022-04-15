from django.shortcuts import render
from .models import newModel

# Create your views here.
def newsView(request):
    context_obj = {
        'news': newModel.objects.all()
    }

    return render(request, 'news.html', context=context_obj)