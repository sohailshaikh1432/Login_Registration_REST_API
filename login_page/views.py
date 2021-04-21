from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from Log_Configuration import log_config_file

# set up logger to handle exceptions
logger = log_config_file.get_logger()


# Create your views here.


def login(request):
    """
    This is a function to check weather user logged-in or Not.
    #param: request which accept "username" & "password"
    #return: HTTPResponse which user Logged-In or Not
    """
    if request == 'POST':
        try:
            user_name = request.POST['username']
            password = request.POST['password']

            authentication = auth.authenticate(username=user_name, password=password)
            if authentication is None:
                return JsonResponse({'status': 'User does not exist'})

        except Exception as excp:
            logger.exception(excp)
            return JsonResponse({'status': 'Login success'})
    else:
        """
        this for GET request
        """
        return JsonResponse({'status': 'failed'})
