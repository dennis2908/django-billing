from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import json
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.template import RequestContext
from django.db.models.query import QuerySet
import random
from django.conf.urls.static import static


from company.models import Company

class CompanyList(ListView):
    model = Company
	
def get_object(request):
	foos = Company.objects.all().order_by('id').reverse()
	if(request.GET['key']):
		foos = foos.raw("select * from company_company WHERE company_code LIKE '%"+request.GET['key']+"%' or company_name LIKE '%"+request.GET['key']+"%' order by id DESC")
	data = serializers.serialize('json', foos)
#print(Company._meta.db_table)
	
	return HttpResponse(data, content_type='application/json')

class CompanyView(DetailView):
	model = Company
	template_name = 'company_view.html'
 
class CompanyCreate(CreateView):
    model = Company
    fields = ['id', 'company_name', 'company_code', 'address', 'phone_number']

class CompanyUpdate(UpdateView):
    model = Company
    fields = ['id', 'company_name', 'company_code', 'address', 'phone_number']
    success_url = reverse_lazy('company_list')

def CompanyDelete(request,id):
	Company.objects.get(pk=id).delete()
	return HttpResponse('deleted')
	
def CompanyGet(request, id):
	foos = Company.objects.filter(pk=id)
	data = serializers.serialize('json', foos)
	return HttpResponse(data, content_type='application/json')

def CompanySave(request):
	if(request.POST['id']):
		obj = Company.objects.get(pk=request.POST['id'])
		obj.company_name = request.POST['company_name']
		obj.company_code = request.POST['company_code']
		obj.address = request.POST['address']
		obj.phone_number = request.POST['phone_number']
	else:	
		obj = Company.objects.create(company_name=request.POST['company_name'],company_code=request.POST['company_code'],address=request.POST['address']
		,phone_number=request.POST['phone_number'])	
	obj.save()
	return HttpResponse('deleted')