from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
import requests
import json
import datetime

@login_required(login_url="login/")
#def home(request):
#    return render(request,"home.html")

def home(request):
    jsonList = []
    req = requests.get('https://api.github.com/users/microsoft')
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parsedData.append(userData)
    return render(request, 'home.html', {'key':data})    
    