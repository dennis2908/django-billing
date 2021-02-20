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
from django.db import connection


from bills.models import Bills
from company.models import Company

class BillList(ListView):
	model = Bills
	template_name = 'bills_list.html'
	
def get_object_bill(request):
	foos = Company.objects
	cursor = connection.cursor()

	if(request.GET['key']):
		cursor.execute("select bill_id,code,company_name,note,bill from company_bills join company_company on company_bills.code = company_company.company_code WHERE company_code LIKE '%"+request.GET['key']+"%' or company_name LIKE '%"+request.GET['key']+"%' order by bill_id DESC", None)
	else:	
		cursor.execute("select bill_id,code,company_name,note,bill from company_bills join company_company on company_bills.code = company_company.company_code order by bill_id DESC", None)
	
	rows = cursor.fetchall()
	pickup_records = json.dumps({'pickups': rows},indent=1) 	
	foos = Company.objects.all().order_by('company_code')
	data = serializers.serialize('json', foos)
#print(Company._meta.db_table)	
	return HttpResponse({'[{"dita":'+pickup_records+',"dennis":'+data+'}]'})

def BillDelete(request,id):
	Bills.objects.get(pk=id).delete()
	return HttpResponse('deleted')
	
def BillGet(request, id):
	foos = Bills.objects.filter(pk=id)
	data = serializers.serialize('json', foos)
	return HttpResponse(data, content_type='application/json')

def BillSave(request):
	if(request.POST['id']):
		obj = Bills.objects.get(pk=request.POST['id'])
		obj.code = request.POST['company_code']
		obj.bill = request.POST['bill']
		obj.note = request.POST['note']
	else:	
		obj = Bills.objects.create(code=request.POST['company_code'],bill=request.POST['bill'],note=request.POST['note'])	
	obj.save()
	return HttpResponse('deleted')