from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.StackedInline):
   model = Choice
   extra = 3


#class QuestionAdmin(admin.ModelAdmin):
    #fieldsets = [
        #(None,               {'fields': ['question_text']}),
       # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
   # ]

inlines = [ChoiceInline]

admin.site.register(Choice)

admin.site.register(Question)
# Register your models here.


#class QuestionAdmin(admin.ModelAdmin):
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
