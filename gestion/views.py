from django.shortcuts import render

# Create your views here.

def indexL(request):
    return render(request, 'gestion/land.html')
