from django.contrib import admin

from .models import Choice, Question

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date", "was_published_recently", "published")
    list_filter = ["pub_date"]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text", "votes")
    list_filter = ("question",)
