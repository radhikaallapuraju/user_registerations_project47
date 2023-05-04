from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def Register(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=Access_RecordForm()
    
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=Access_RecordForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            NSTO=tfd.save(commit=False)
            NSTO.save()

            NSWO=wfd.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()
            
            NSAO=afd.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('data is register successfully...')
        else:
            return HttpResponse('date is not valid..')
    
    return render(request,'register.html',d)