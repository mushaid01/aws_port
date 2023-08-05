from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from pytz import timezone
from blog.forms import PostForm,CommentForm
from django.utils import timezone
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import  datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def LikeView(request,pk):
    post=get_object_or_404(Post,pk=pk)
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('blog:post_detail',args=[str(pk)] ))
    
    



class AboutView(TemplateView):
    template_name='blog/about.html'


class PostListView(ListView):
    model=Post
    

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

class PostDetailView(DetailView):
    model=Post
    def get_context_data(self, *args,**kwargs):
        context=super(PostDetailView,self).get_context_data(**kwargs)
        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForm
    model=Post
# @login_required
# def CreatePostView(request,pk):
#     post=get_object_or_404(Post,pk=pk)
#     if request.method=="POST":
#         form=PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:post_detail',pk=post.pk)
#     else:
#             form=PostForm()
#     return render(request,'blog/post_form.html',{'form':form})


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForm
    model=Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('blog:post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


##########################################################
##########################################################


@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)
