from django.views.generic import View
from django.shortcuts import render
class HomeView(View):
    """
    get request = Es lo que pide la informacion para que tu puedas ver
    host request = Es lo que tu envias para mandar al servidor
    """
    def get(self, request, *args, **kwargs):
        context ={
            
        }
        return render(request, 'index.html', context)
        