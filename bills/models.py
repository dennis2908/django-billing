from django.db import models
from django.urls import reverse

class Bills(models.Model):
	bill_id = models.AutoField(primary_key=True)
	code = models.CharField(max_length=200,default="")
	note = models.CharField(max_length=200,default="")
	bill = models.IntegerField(default=170)

	class Meta:
		db_table = 'company_bills'
		
	def __str__(self):
		return self.id,self.company_code,self.note,self.bill

	def get_absolute_url(self):
		return reverse('bill_list', kwargs={'pk': self.pk})