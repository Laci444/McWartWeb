from django.shortcuts import render
from .models import newModel

# Create your views here.
def newsView(request):
    search = request.GET.get('search', False)
    if search:
        context_obj = {
            'news': newModel.objects.filter(title__contains=request.GET.get('search', True))
        }
    else:
        context_obj = {
            'news': newModel.objects.all()
        }

    return render(request, 'news.html', context=context_obj)