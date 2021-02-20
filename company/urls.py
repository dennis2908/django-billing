from django.urls import path

from . import views

urlpatterns = [
	path('', views.CompanyList.as_view(), name='company_list'),
	path('view/', views.get_object),
	path('save/', views.CompanySave),
	path('get/<int:id>', views.CompanyGet, name='company_get'),
	path('delete/<int:id>', views.CompanyDelete, name='company_delete'),
]