from reviews.models import Review
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermissionClass
from rest_framework import generics
from reviews.serializers import ReviewSerializer

class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissionClass,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissionClass,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
