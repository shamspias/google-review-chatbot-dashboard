from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreate(generics.ListCreateAPIView):
    """
    List all reviews, or create a new review.
    """
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
