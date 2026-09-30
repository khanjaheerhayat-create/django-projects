from django.shortcuts import render

# Create your views here.
def movie_view(request):
    head_msg='Movie Information'
    sub_msg1='OG was block buster'
    sub_msg2='Planning for aashique-3'
    sub_msg3="don't go movie read django"
    type='movies'
    my_dict={'head_msg':head_msg,sub_msg1:sub_msg1,sub_msg2:sub_msg2,sub_msg3:sub_msg3,'type':type}
    return render(request,'testapp/index.html',context=my_dict)
def sport_view(request):
    head_msg='Sport Information'
    sub_msg1='ipl start soon'
    sub_msg2='Messi came to hyderabad'
    sub_msg3="Revanth reddy played well ith revanth reddy"
    type='sports'
    my_dict={'head_msg':head_msg,sub_msg1:sub_msg1,sub_msg2:sub_msg2,sub_msg3:sub_msg3,'type':type}
    return render(request,'testapp/index.html',context=my_dict)
def politic_view(request):
    head_msg='Politics Information'
    sub_msg1='Indian PM was modi ji'
    sub_msg2='AP CM was CBN'
    sub_msg3="AP DY CM was pawan Kalyan"
    type='politics'
    my_dict={'head_msg':head_msg,sub_msg1:sub_msg1,sub_msg2:sub_msg2,sub_msg3:sub_msg3,'type':type}
    return render(request,'testapp/index.html',context=my_dict)