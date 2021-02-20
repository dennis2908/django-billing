from django.db import models
from django.urls import reverse

class Company(models.Model):
	id = models.AutoField(primary_key=True)
	company_name = models.CharField(max_length=200,default="")
	company_code = models.CharField(max_length=200,default="")
	address = models.CharField(max_length=200,default="")
	phone_number = models.CharField(max_length=200,default="")

	def __str__(self):
		return self.id,self.company_name,self.company_code,self.address,self.phone_number

	def get_absolute_url(self):
		return reverse('company_list', kwargs={'pk': self.pk})