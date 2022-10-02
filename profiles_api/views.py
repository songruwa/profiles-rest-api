from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    # format: format suffix at the endpoint of URL
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Give you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        # convert response into json
        # use dictionary to convert to json
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
