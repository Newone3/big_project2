from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Prispevky
# Create your views here.
def post_list(request):
    prispevky = Prispevky.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'prispevky/post_list.html', {'prispevky': prispevky})

def post_detail(request, pk):
    prispevky = get_object_or_404(Prispevky, pk=pk)
    return render(request, 'prispevky/post_detail.html', {'prispevky': prispevky})
