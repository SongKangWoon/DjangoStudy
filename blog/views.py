from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.
def post_list(request):
    posts = Post.published.all() # published 된 게시물들을 다 가지고옴

    return render(request,'blog/post/list.html',{'posts':posts})

def post_detail(request, id):
    # try:
    #
    #     post = Post.published.get(id=id) # id로 가지고옴
    #
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")

    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED) # 매개변수와 일치하는 객체를 찾거나 해당 객체가 없으면 http404(찾을수없음) 예외를 발생시킴

    return render(request,'blog/post/detail.html',{'post':post})