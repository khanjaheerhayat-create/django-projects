from django.shortcuts import render
import datetime,random,time
# Create your views here.
def astro(request):
    msg_list=[
        'The golden days are head',
        'better sleep do not go to office',
        'Tomorrow will be the best day of your life',
        'very soon you will get job',
        'tomorrow is the perfect day of your life'
    ]
    name=['junaid','kala','jaheer','jahangir','jabir','samaira']
    date=datetime.datetime.now()
    h=int(time.strftime('%H'))
    if h<12:
        s='good morning'
    elif h<16:
        s='good Afternoon'
    elif h<21:
        s='good evening'
    else:
        s='good night'
    msg=random.choice(msg_list)
    name=random.choice(name)
    my_dict={'name':name,'msg':msg,'date':date,'wish':s}
    return render(request,'testapp/index.html',my_dict)