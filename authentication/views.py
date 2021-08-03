from rest_framework.generics import GenericAPIView
from .serializers import UserSerializes
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class RegisterView(GenericAPIView):
    serializer_class = UserSerializes
    def post(self,request):
        serializer = UserSerializes(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)