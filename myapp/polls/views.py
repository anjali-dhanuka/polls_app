from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseNotFound
from polls.models import Question , Choice

#def index(request):
def detail(request, question_id):
   try:
     question = Question.objects.get(pk=question_id)
   except:
     raise Http404("question doesn't exist")
   return render(request,'polls/details.html',{'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)          


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)





