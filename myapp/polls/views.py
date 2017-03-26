from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from polls.models import Question , Choice
from django.core.urlresolvers import reverse

#def index(request):
def detail(request, question_id):
   try:
     question = Question.objects.get(pk=question_id)
   except:
     raise Http404("question doesn't exist")
   return render(request,'polls/details.html',{'question': question})


def results(request, question_id):
    question= get_object_or_404(Question,pk=question_id)    
    return render(request,'polls/results.html',{'question': question})

def vote(request, question_id):
    p=get_object_or_404(Question, pk=question_id)
    try:
       selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(Keyerror, Choice.DoesNotExist):
       return render(request,'polls/details.html', {
          'question': p,
          'error_message':"you didn't select a choice.",
        })  
    else:
       selected_choice.votes+=1
       selected_choice.save()
       return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))    
 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)





