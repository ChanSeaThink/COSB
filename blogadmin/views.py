# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse

from blogadmin.forms import blogArticleForm, blogCommentForm, fatherClassForm, childClassForm
from blogadmin.models import blogArticle,blogComment, fatherClass, childClass
# Create your views here.
def back(request):
	return render_to_response('backEnd.html')

#fc表示父类输入页面的响应函数。
def fc(request):
    if request.method == 'POST':
        form = fatherClassForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fatherClassObj = fatherClass()
            fatherClassObj.name = data['name']
            fatherClassObj.contentnum = 0
            fatherClassObj.childnum = 0
            fatherClassObj.save()
        else:
            return HttpResponse('data error')
    else:
        form = fatherClassForm()
    return render_to_response('inputdata.html',{'form':form})

#cc表示子类输入页面的响应函数。
def cc(request):
    '''
    由于在childClassForm类中，为了可以动态改变下拉菜单的选项值，所以重新定义了fatherclass的域，所以在
    重新导入的时候必须也带上choices的值。而且choices也必须是一个有效的值。
    '''
    choices = []
    fatherClass_data = fatherClass.objects.all()
    for dl in fatherClass_data:
        choices.append((dl.id,dl.name))
    if request.method == 'POST':
        form = childClassForm(choices,request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #fatherClassObj表示fatherClass表中的某一行数据（根据id选择）。
            fatherClassObj = fatherClass.objects.get(id = data['fatherclass'])
            #childClassObj创建新的childClass表的数据行。
            childClassObj = childClass()
            childClassObj.name = data['name']
            childClassObj.contentnum = 0
            childClassObj.fatherclass = fatherClassObj.name
            childClassObj.fatherclassid = fatherClassObj
            childClassObj.save()
            fatherClassObj.childnum += 1
            fatherClassObj.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('error')
    else:
        form = childClassForm(choices)
    return render_to_response('inputdata.html',{'form':form})

#ba表示文章的输入页面的响应函数。
def ba(request):
    fcc = []
    ccc = []
    fatherClass_data = fatherClass.objects.all()
    childClass_data = childClass.objects.all()
    for d in fatherClass_data:
        fcc.append((d.id, d.name))
    for d in childClass_data:
        fcc.append((d.id, d.name))
    if request.method == 'POST':
        return HttpResponse('Hello')
    else:
        form = blogArticleForm(fcc, ccc)
    return render_to_response('inputdata.html',{'form':form})

def bc(request):
    form = blogCommentForm()
    return render_to_response('inputdata.html',{'form':form})
