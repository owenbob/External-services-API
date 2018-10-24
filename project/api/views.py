from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class SetUp(APIView):
    """
    Class to check whether django version 1.11 and 
    django restframework have been properly intergrated.
    """
    def get(self, request):
        message = " You have succesfully setup Django 1.11 and DRF"
        return Response(message)

