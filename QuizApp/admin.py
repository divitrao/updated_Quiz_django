from django.contrib import admin
from .models import Quiz, Question, CorrectAnswer, UserAnswer, Progress


class OptionInline(admin.TabularInline):
    model = CorrectAnswer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline,]
    list_display = ['quizId', 'type', 'marks', 'question'] 


admin.site.register(Quiz)
admin.site.register(UserAnswer)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Progress)

