from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.http import HttpResponse,JsonResponse
# Create your views here.
import json
from rest_framework.decorators import api_view
from .models import User,Project,Gug
from .serializers import GugSerializer


def search(request):
    if request.method == 'GET':
        project_id = request.GET.get('project_id')
        user_id = request.GET.get('user_id',None)
        project  = get_object_or_404(Project,id=project_id)
        if user_id is not None:
            user = get_object_or_404(User,id=user_id)
            gug_fil = Gug.objects.all().filter(project=project,user=user)
        else:
            gug_fil = Gug.objects.all().filter(project=project)
        gug_json = {'bugs':list(gug_fil.values('id','user__username','project__name_project','rate'))}

        return JsonResponse(gug_json)






