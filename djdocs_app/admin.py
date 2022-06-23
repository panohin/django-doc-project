from django.contrib import admin
from . import models


class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
