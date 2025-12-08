from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "checked", "created_at")
    list_filter = ("checked",)
    search_fields = ("full_name", "email", "text")