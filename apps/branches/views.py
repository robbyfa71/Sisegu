from django.shortcuts import render

# Create your views here.
def branches_list (request):
    return render(request, 'branches/index.html')