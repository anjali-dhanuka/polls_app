from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
   model = Choice
   extra = 3

class QuestionAdmin(admin.ModelAdmin):
   list_display = ('question_text','pub_date','was_published_recently')
   list_filter=['pub_date']
   search_fields=['question_text']
#class QuestionAdmin(admin.ModelAdmin):
    #fieldsets = [
        #(None,               {'fields': ['question_text']}),
       # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
   # ]

inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
   list_display = ('question','choice_text','votes')



admin.site.register(Choice,ChoiceAdmin)

admin.site.register(Question,QuestionAdmin)
# Register your models her_filter]

#class QuestionAdmin(admin.ModelAdmin):
#def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
   # return HttpResponse(response % question_id)

#def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
