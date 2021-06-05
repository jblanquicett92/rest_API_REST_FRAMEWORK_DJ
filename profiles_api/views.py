from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    #Test API VIEW
    def get(self, request, format=None):
        
        an_APIView = [
            'Jorge',
            'Blanquicett',
            'Colombia',
        ]
        
        return Response({'message': 'Hello world there', 'an_APIView': an_APIView  })
