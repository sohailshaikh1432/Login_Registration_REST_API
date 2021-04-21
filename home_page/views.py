from django.shortcuts import render
from Log_Configuration import log_config_file
from django.http import HttpResponse
# Create your views here.
# set up logger to handle exceptions
logger = log_config_file.get_logger()


def home(request):
    """
    #param: request from user
    #return: return home.html
    """
    try:
        return render(request, 'home.html')
    except Exception as ecxep:
        logger.exception(ecxep)



