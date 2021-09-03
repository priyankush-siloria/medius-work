from django.db import models
import uuid


class RetrivedData(models.Model):
	name = models.CharField(verbose_name='Customer Name',max_length=120,null=True,blank=True)
	due_amount = models.IntegerField(verbose_name='Due Amount',null=True,blank=True)
	template_id = models.IntegerField(verbose_name='Template ID',null=True,blank=True)
	batch_id =  models.IntegerField(verbose_name='Batch ID',null=True,blank=True)
	mobile_no = models.CharField(verbose_name='Mobile Number',max_length=120,null=True,blank=True)
	loan_account_no = models.CharField(verbose_name='Loan Account Number',max_length=120,null=True,blank=True)
	status = models.BooleanField(default=False)
	due_date = models.DateTimeField(null=True,blank=True)
	scheduled_at = models.DateTimeField(null=True,blank=True)
	created_at = models.DateTimeField(null=True,blank=True)
	updated_at = models.DateTimeField(null=True,blank=True)
	response = models.JSONField(null=True,blank=True)


class ProcessData(models.Model):
	loan_account_no = models.CharField(verbose_name='Loan Account Number',max_length=120,null=True,blank=True)
	mobile_no = models.CharField(verbose_name='Mobile Number',max_length=120,null=True,blank=True)
	template_id = models.IntegerField(verbose_name='Template ID',null=True,blank=True)
	request = models.JSONField()
	response = models.JSONField()
	audio_url = models.URLField(max_length=200,null=True,blank=True)
	created_at = models.DateTimeField()

	def __str__(self):
		return self.loan_account_no