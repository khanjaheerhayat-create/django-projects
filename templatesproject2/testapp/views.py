from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    my_dict={'date':date}
    return render(request,'testapp/wish.html',context=my_dict)