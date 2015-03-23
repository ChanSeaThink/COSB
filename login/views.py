# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse

import Image, ImageDraw, ImageFont, ImageFilter, random
from hashlib import sha1

from datetime import datetime
import cStringIO

from login.forms import registForm
from login.models import userInfo

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def login(request):
    error = ''#控制报错区域显示隐藏的Flag
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        valicode = request.POST['valicode']
        userInfo_data = userInfo.objects.get(username = username)
        password_db = userInfo_data.password
        createtime_db = userInfo_data.createtime
        sh = sha1()
        sh.update(password + str(createtime_db)[0:19])
        sh1 = sha1()
        sh1.update(valicode)
        if sh1.hexdigest() == request.session['CAPTCHA']:
            if sh.hexdigest() == password_db:
                return HttpResponse('登录成功!')
            else:
                return HttpResponse('密码错误!')
        else:
            error = 'Y'
            
        #print str(createtime_db)[0:19]
        #print password_db
        #print sh.hexdigest()
    return render_to_response('login.html', {'error':error})
    #username = request.POST.get('username','unknown')可以设置默认的方法。
    #password = request.POST.get('password','unknown')
    #print username
    #print password
    #userInfo_list = userInfo.objects.all()
    #userInfo获取所有数据
    #userInfo_list = userInfo.objects.all()获取数据表下的所有数据。
    #print userInfo_list[0].nickname 此注释代码可以在终端显示从mysql读出的utf8编码的数据。__unicode__无法读取中文。
    #users = userInfo.objects.filter(username__exact=username,password__exact=password)直接做匹配的写法。

def getCAPTCHA(request):
    sh = sha1()
    sh.update(str(datetime.now()))
    sh_src = sh.hexdigest()
    code = sh_src[0:4]
    #string = {'number':'12345679','litter':'ACEFGHKMNPRTUVWXY'}
    background = (random.randrange (230,255),random.randrange(230,255),random.randrange(230,255))
    line_color = ['red', 'blue', 'yellow', 'green', 'brown']
    img_width = 120
    img_height = 42 
    font_color = ['black','red', 'blue', 'green', 'brown']
    point_color = ['red', 'blue', 'yellow', 'green', 'brown']
    font_size = 25
    font = ImageFont.truetype('msyh.ttf',font_size)
    #新建画布
    im = Image.new('RGB',(img_width,img_height),background)
    draw = ImageDraw.Draw(im)
    #code = random.sample(string['litter'],4)
    #新建画笔
    draw = ImageDraw.Draw(im)
    #干扰点(70表示30%的概率)
    for w in range(img_width):
        for h in range(img_height):
            tmp = random.randrange(1,100)
            if tmp > 90:
                draw.point((w, h), fill=(random.choice(point_color)))
    #画干扰线
    for i in range(random.randrange(5,8)):
        xy = (random.randrange(0,img_width),random.randrange(0,img_height),
              random.randrange(0,img_width),random.randrange(0,img_height))
        draw.line(xy,fill=(random.choice(line_color)),width=1)
    #写入验证码文字
    x = 10
    for i in code:
        y = random.randrange(0,7)
        draw.text((x,y), i, font=font, fill=random.choice(font_color))
        x += 20
    del x
    del draw
    params = [1 - float(random.randint(1, 2)) / 100,
                  0,
                  0,
                  0,
                  1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500,
                  0.001,
                  float(random.randint(1, 2)) / 500
                  ]
    im = im.transform((120,42), Image.PERSPECTIVE, params) # 创建扭曲
    buf = cStringIO.StringIO()
    im.save(buf, 'gif')
    request.session['CAPTCHA'] = code
    return HttpResponse(buf.getvalue(), 'image/gif')

def regist(request):
    if request.method == 'POST':
        form =registForm(request.POST)
        if form.is_valid():
            registData = form.cleaned_data
            #print registData['username']
            #print registData['password']
            #print registData['password2']
            #print registData['nickname']
            if registData['password'] == registData['password2']:
                nt = datetime.now()
                #print nt
                shpw = sha1()
                shpw.update(registData['password'] + str(nt)[0:19])#
                #print str(nt)[0:19]
                pw = shpw.hexdigest()
                userDataObj = userInfo()
                userDataObj.username = registData['username']
                userDataObj.password = pw
                userDataObj.nickname = registData['nickname']
                userDataObj.createtime = nt
                userDataObj.save()
                return HttpResponse('ok')
            else:
                return HttpResponse('两次密码不想等。')
    else:
        form = registForm()
    return render_to_response('regist.html',{'form':form})