from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin for Review model
    """
    list_display = ('author', 'review_text', 'response', 'created_at')
    search_fields = ('author', 'review_text', 'response')
    list_filter = ('created_at',)


admin.site.register(Review, ReviewAdmin)
