from django.contrib import admin

# Register your models here.

from .models import Course
from .models import Question

class QuestionA(admin.ModelAdmin):
    list_display = ('course', 'question', 'marks')

admin.site.register(Course)
admin.site.register(Question, QuestionA)