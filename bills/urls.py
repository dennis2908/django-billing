from django.urls import path

from . import views

urlpatterns = [
	path('', views.BillList.as_view(), name='bill_list'),
	path('view/', views.get_object_bill),
	path('save/', views.BillSave),
	path('get/<int:id>', views.BillGet, name='bill_get'),
	path('delete/<int:id>', views.BillDelete, name='bill_delete'),
]