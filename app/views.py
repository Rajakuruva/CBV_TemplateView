from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponse
from app.forms import *
# Create your views here.
class Template_form(TemplateView):
    template_name='Template_form.html'
    def get_context_data(self,**kwargs):
        CO=super().get_context_data(**kwargs)
        TO=Topicform()
        CO["TO"]=TO
        return CO
    def post(self,request):
        CTO=Topicform(request.POST)
        if CTO.is_valid():
            CTO.save()
        return HttpResponse("Data insrted successfully!!!")

class CBNSD(Template_form):
    template_name='CBNSD.html'
    def get_context_data(self, **kwargs):
        x=super().get_context_data(**kwargs)
        x["Name"]="Rajasekhar"
        x['Age']=20
        return x