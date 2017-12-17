#!/root/myenv1/bin python3.5
# -*- coding: utf-8 -*-

from django import forms
from  .models import Comment

# 创建评论的表单
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]