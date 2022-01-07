from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class BlogListView(View):
    def get(self, request,*args, **kwargs):
        contexto = {
            
        }
        return render(request, 'blo_list.html', contexto)
