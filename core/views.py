from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View



# Create your views here.


class Index(View):
    def get(self, request):
        
        return render(request, 'core/index.html')

    
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
