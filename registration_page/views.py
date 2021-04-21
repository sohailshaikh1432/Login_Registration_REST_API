from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from Log_Configuration import log_config_file

# Create your views here.
logger = log_config_file.get_logger()


def registration(request):
    """
    This function use to Register user.
    #param: username,firstname,lastname,email_id,password
    #return: HTTPRespond that user register successfully.
    """
    if request.method == 'POST':
        try:
            user_name = request.POST['username']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email_id']
            password = request.POST['password']

            authentication = User.objects.create_user(username=user_name,
                                                      first_name=first_name,
                                                      last_name=last_name,
                                                      email=email,
                                                      password=password)
            authentication.save()
            print("User created")
            return JsonResponse({'status': 'User registration is successful'})
        except Exception as excp:
            logger.exception(excp)
    else:
        return JsonResponse({'status': 'User registration is failed'})
