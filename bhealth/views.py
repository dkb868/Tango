from django.shortcuts import render

def index(request):
    context_dict = {}
    return render(request, 'bhealth/index.html', context_dict)