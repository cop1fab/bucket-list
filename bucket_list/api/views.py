# api/views.py

from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
        """This class handles the http GET, PUT and DELETE requests."""
        print('Yeah')
        queryset = Bucketlist.objects.all()
        serializer_class = BucketlistSerializer
