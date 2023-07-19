from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View """

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods a function (get, post, patch, put, delete)',
        'Is Similar to a traditional Djngo View',
        'Gives you the most control over you application login',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview' : an_apiview})
