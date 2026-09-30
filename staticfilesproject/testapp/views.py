from django.shortcuts import render

# Create your views here.
def result_view(request):
    subject={'s1':'Python','s2':'django','s3':'restapi','s4':'numpy and pandas'}
    return render(request,'testapp/result.html',{'subject':subject})