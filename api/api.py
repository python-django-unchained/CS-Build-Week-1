from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json
from uuid import uuid4
# from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
import bcrypt

# @csrf_exempt
# @api_view(["POST"])
# def register(request):
#     data = json.loads(request.body)
#     new_user = User.objects.create_user(username=data["username"], password=data["password"])
#     new_user.save()
#     return JsonResponse({ "username": new_user.username })

@csrf_exempt
@api_view(["POST"])
def login(request):
    data = json.loads(request.body)
    password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    new_user = Cowboy(uuid4(), data["username"], password)
    # cowboy_username = data["username"]
    # cowboy_password = data["password"]
    new_user.initialize()
    return JsonResponse({ "username": new_user.username })
