from django.db import models


class Review(models.Model):
    """
    Model for Review
    """
    author = models.CharField(max_length=255)
    review_text = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.review_text}'
