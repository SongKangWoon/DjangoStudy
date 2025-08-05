from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
    post_list = Post.published.all() # published 된 게시물들을 다 가지고옴

    # https://docs.djangoproject.com/en/4.1/ref/paginator/
    paginator = Paginator(post_list, 3) # 페이지당 반환할 객체 수와 함께 Paginator 클래스를 인스턴스화 합니다.
    page_number = request.GET.get('page',1) # HTTP GET 매개 변수 PAGE를 조회해서 그 값을 PAGE_NUMBER 변수에 저장합니다.
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # 페이지 넘버가 정수가 아닌 경우 첫 번째 페이지를 전달
        posts = paginator.page(1)
    except EmptyPage:
        # 페이지 번호가 범위를 벗어난 경우 결과의 마지막 페이지를 전달
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,slug =post, publish__year = year, publish__month = month, publish__day = day)
    return render(request,'blog/post/detail.html',{'post':post})