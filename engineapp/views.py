from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import CreateView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import (
    RetrivedData,
    ProcessData
)
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import (
	RetrivedDataSerializer,
	)
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import requests


class RetrivedDataView(APIView):
	serializer_class = RetrivedDataSerializer
	permission_classes = (AllowAny,)

	def post(self, request):
		USER_AGENT='Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
		headers = {'User-Agent': USER_AGENT}
		response_data = requests.get(request.data['requested_url'], headers=headers).json()
		obj, status = RetrivedData.objects.get_or_create(batch_id=response_data['batch_id'],template_id=response_data['template_id'],mobile_no=response_data['mobile_no'])
		
		if status:
			serializer = self.serializer_class(obj, data=response_data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return Response({"info":"Saved responded data at Server."})

	def get(self,request,pk):
		retrived_obj = RetrivedData.objects.get(id=pk)
		serializer = RetrivedDataSerializer(retrived_obj,many=False)
		return Response(serializer.data)


	def delete(self,request,pk):
		retrived_obj = get_object_or_404(RetrivedData,id=pk)
		retrived_obj.delete()
		return Response({"info":"RetrivedData has been deleted"})
