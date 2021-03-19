from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
# from blog.templatetags import extras

# Create your views here.
def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    comments= BlogComment.objects.filter(post=post, parent=None)
    # replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    # replyDict={}
    # for reply in replies:
    #     if reply.parent.sno not in replyDict.keys():
    #         replyDict[reply.parent.sno]=[reply]
    #     else:
    #         replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, }
    return render(request, "blog/blogPost.html", context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("blogPost", args=[str(pk)]))

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")
        # if parentSno=="":
        #     comment=BlogComment(comment= comment, user=user, post=post)
        #     comment.save()
        #     messages.success(request, "Your comment has been posted successfully")
        # else:
        #     parent= BlogComment.objects.get(sno=parentSno)
        #     comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
        #     comment.save()
        #     messages.success(request, "Your reply has been posted successfully")

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments, 'user': request.user}
    return render(request, "blog/blogPost.html", context)

