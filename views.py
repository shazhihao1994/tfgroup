# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from tf.models import User,Equipment,LendEquipment,LendingEquipment,GiveEquipment,DeleteEquipment
from django.contrib.auth.decorators import login_required
from django.template import RequestContext 
from django.contrib import auth

def main_page(request):
    
    output = '''
    <html>
    <head><title>%s</title></head>
    <body align="center" background="/site_media/hit.jpg">
    <h1 align="center">%s</h1>
    <p align="center">
    <p>&nbsp;</p>
    <p><a href='http://127.0.0.1:8000/registe/'>用户注册</a></p>
    <p><a href='http://127.0.0.1:8000/login/'>用户登录</a></p>
    <p><a href='http://127.0.0.1:8000/admin/'>管理员登录</a></p></p>
    </body>
    </html>
    ''' % (  
    '科研设备管理系统',
    '欢迎使用科研设备管理系统',
    )
    return HttpResponse(output)

def registe(request):
    
    if request.POST:
        post = request.POST
        new_people = User(
        Username = post["Username"],
        Password = post["Password"],
        Leixing  = post["L"],
        )
        new_people.save()        
        return render_to_response("registeok.html",context_instance=RequestContext(request))    
    return render_to_response("registe.html",context_instance=RequestContext(request))
    
def login(request):
    
    if request.POST:
        post = request.POST
        for user in User.objects.all():
            if user.Username == post["Username"] and user.Password == post["Password"]:
                request.session['Leixing'] = user.Leixing
                return render_to_response("search_form.html")
        return render_to_response("loginfail.html", context_instance=RequestContext(request))
    return render_to_response("login.html", context_instance=RequestContext(request))

def search_form(request):
    
    return render_to_response('search_form.html')
    
def search_result(request):
    
    if 'a' in request.GET and request.GET['a']:
        a = request.GET['a']
        numbers = Equipment.objects.filter(Name__contains=a)
        return render_to_response('search_result.html',{'numbers':numbers})
    if 'b' in request.GET and request.GET['b']:
        b = request.GET['b']
        numbers=Equipment.objects.filter(Number__contains=b)
        return render_to_response('search_result.html',{'numbers':numbers})
    if 'c' in request.GET and request.GET['c']:
        c = request.GET['c']
        numbers=Equipment.objects.filter(Model__contains=c)
        return render_to_response('search_result.html',{'numbers':numbers})
    if 'd' in request.GET and request.GET['d']:
        d = request.GET['d']
        numbers=Equipment.objects.filter(Price__contains=d)
        return render_to_response('search_result.html',{'numbers':numbers})
    if 'e' in request.GET and request.GET['e']:
        e = request.GET['e']
        numbers=Equipment.objects.filter(Prodate__contains=e)
        return render_to_response('search_result.html',{'numbers':numbers})
    if 'f' in request.GET and request.GET['f']:
        f = request.GET['f']
        numbers=Equipment.objects.filter(Buydate__contains=f)
        return render_to_response('search_result.html',{'numbers':numbers})
        
    else:   
        return render_to_response('search_form.html', {'error': True})
        
def summary(request):
    
    return render_to_response('summary.html')
 
def add_form(request):
    
    return render_to_response('add_form.html')
    
def add_result(request):
    
    if 'a' in request.GET and request.GET['a']:
        a = request.GET['a']
    if 'b' in request.GET and request.GET['b']:
        b = request.GET['b']
    if 'c' in request.GET and request.GET['c']:
        c = request.GET['c']
    if 'd' in request.GET and request.GET['d']:
        d = request.GET['d']
    if 'e' in request.GET and request.GET['e']:
        e = request.GET['e']
    if 'f' in request.GET and request.GET['f']:
        f = request.GET['f']
    L = request.session['Leixing']
    if L!=b[:1]:
        return render_to_response('out_of_range.html')
    p = Equipment(Name=a,Number=b,Model=c,Price=d,Prodate=e,Buydate=f)
    p.save()
    return render_to_response('result.html', {'type':'添加','result':'成功'})

def computer(request):
    
    numbers = Equipment.objects.filter(Number__contains='-C')
    length = len(numbers)
    prices = 0
    for i in range(0,length):
        prices += int(numbers[i].Price)
    return render_to_response('computer.html',{'numbers':numbers,'length':length,'prices':prices})

def robot(request):
    
    numbers = Equipment.objects.filter(Number__contains='-R')
    length = len(numbers)
    prices = 0
    for i in range(0,length):
        prices += int(numbers[i].Price)
    return render_to_response('robot.html',{'numbers':numbers,'length':length,'prices':prices})

def sensor(request):
    
    numbers = Equipment.objects.filter(Number__contains='-S')
    length = len(numbers)
    prices = 0
    for i in range(0,length):
        prices += int(numbers[i].Price)
    return render_to_response('sensor.html',{'numbers':numbers,'length':length,'prices':prices})
    
def update(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    member = Equipment.objects.get(Number=q)
    return render_to_response('update.html', {'member': member})

def lend(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    member = Equipment.objects.get(Number=q)
    return render_to_response('lend.html', {'member': member})
    
def give(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    member = Equipment.objects.get(Number=q)
    return render_to_response('give.html', {'member': member})
        
def delete(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    member = Equipment.objects.get(Number=q)
    return render_to_response('delete.html', {'member': member})
        
def update_submit(request):
    
    if 'a' in request.GET and request.GET['a']:
        a = request.GET['a']
    if 'b' in request.GET and request.GET['b']:
        b = request.GET['b']
    if 'c' in request.GET and request.GET['c']:
        c = request.GET['c']
    if 'd' in request.GET and request.GET['d']:
        d = request.GET['d']
    if 'e' in request.GET and request.GET['e']:
        e = request.GET['e']
    if 'f' in request.GET and request.GET['f']:
        f = request.GET['f']
    L = request.session['Leixing']
    if L!=b[:1]:
        return render_to_response('out_of_range.html')
    Equipment.objects.filter(Number=b).update(Name=a,Number=b,Model=c,Price=d,Prodate=e,Buydate=f)
    return render_to_response('result.html', {'type':'更新','result':'成功'})

def lend_submit(request):
    
    if 'a' in request.GET and request.GET['a']:
        a = request.GET['a']
    if 'b' in request.GET and request.GET['b']:
        b = request.GET['b']
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    numbers = Equipment.objects.get(Number=q)
    L = request.session['Leixing']
    if L!=q[:1]:
        return render_to_response('out_of_range.html')
    p = LendEquipment(LName=numbers.Name,LNumber=numbers.Number,LModel=numbers.Model,LPrice=numbers.Price,LProdate=numbers.Prodate,LBuydate=numbers.Buydate)
    p.save()
    Equipment.objects.get(Number=q).delete()
    return render_to_response('result.html', {'type':'借出申请提交','result':'成功'})

def give_submit(request):
    
    if 'a' in request.GET and request.GET['a']:
        a = request.GET['a']
    if 'b' in request.GET and request.GET['b']:
        b = request.GET['b']
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    numbers=Equipment.objects.get(Number=q)
    L = request.session['Leixing']
    if L!=q[:1]:
        return render_to_response('out_of_range.html')
    p = GiveEquipment(GName=numbers.Name,GNumber=numbers.Number,GModel=numbers.Model,GPrice=numbers.Price,GProdate=numbers.Prodate,GBuydate=numbers.Buydate)
    p.save()
    Equipment.objects.get(Number=q).delete()
    return render_to_response('result.html', {'type':'调拨申请提交','result':'成功'})
        
def delete_submit(request):
    
    if 'a' in request.GET and request.GET['a']:
        a = request.GET['a']
    if 'b' in request.GET and request.GET['b']:
        b = request.GET['b']
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    numbers=Equipment.objects.get(Number=q)
    L = request.session['Leixing']
    if L!=q[:1]:
        return render_to_response('out_of_range.html')
    p = DeleteEquipment(DName=numbers.Name,DNumber=numbers.Number,DModel=numbers.Model,DPrice=numbers.Price,DProdate=numbers.Prodate,DBuydate=numbers.Buydate)
    p.save()
    Equipment.objects.get(Number=q).delete()
    return render_to_response('result.html', {'type':'报废申请提交','result':'成功'})
    
def return_submit(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    Lingnumbers=LendingEquipment.objects.get(LingNumber=q)
    L = request.session['Leixing']
    if L!=q[:1]:
        return render_to_response('out_of_range.html')
    p = Equipment(Name=Lingnumbers.LingName,Number=Lingnumbers.LingNumber,Model=Lingnumbers.LingModel,Price=Lingnumbers.LingPrice,Prodate=Lingnumbers.LingProdate,Buydate=Lingnumbers.LingBuydate)
    p.save()
    LendingEquipment.objects.get(LingNumber=q).delete()
    return render_to_response('result.html', {'type':'归还','result':'成功'})
 
def to_be_lent(request):
    
    Lnumbers = LendEquipment.objects.all()
    return render_to_response('to_be_lent.html',{'Lnumbers':Lnumbers})

def lending(request):
    
    Lingnumbers = LendingEquipment.objects.all()
    return render_to_response('lending.html',{'Lingnumbers':Lingnumbers})

def to_be_given(request):
    
    Gnumbers = GiveEquipment.objects.all()
    return render_to_response('to_be_given.html',{'Gnumbers':Gnumbers})

def to_be_deleted(request):
    
    Dnumbers = DeleteEquipment.objects.all()
    return render_to_response('to_be_deleted.html',{'Dnumbers':Dnumbers})
  
