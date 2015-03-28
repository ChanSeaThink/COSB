# -*- coding: utf8 -*-
from django import forms

class blogArticleForm(forms.Form):
    blogtitle = forms.CharField()
    blogcontent = forms.CharField(widget = forms.Textarea)

    def __init__(self, chf, chc, *args, **kwargs):
        super(blogArticleForm,self).__init__(*args, **kwargs)
        self.fields['fatherclass'].choices = chf
        self.fields['childclass'].choices = chc

    fatherclass = forms.ChoiceField()
    childclass = forms.ChoiceField()

class blogCommentForm(forms.Form):
    nickname = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget = forms.Textarea)
    #contentid = forms.IntegerField()
    def __init__(self, ch, *args, **kwargs):
        super(blogCommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].choices = ch
    content = forms.ChoiceField()

class fatherClassForm(forms.Form):
    name = forms.CharField()

class childClassForm(forms.Form):
    '''
    __init__函数用于实现choicefiled实现动态获取选项之。
    '''
    name = forms.CharField()

    def __init__(self, ch, *args, **kwargs):
        super(childClassForm, self).__init__(*args, **kwargs)
        self.fields['fatherclass'].choices = ch
    fatherclass = forms.ChoiceField()