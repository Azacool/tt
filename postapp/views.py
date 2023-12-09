from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
       context = super(PostListView,self).get_context_data(**kwargs)
       posts = Post.objects.all()
       context['posts'] = posts
       return context
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ('title', 'short_desc', 'body',)
    success_url = reverse_lazy('index')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    context_object_name = 'post'
    fields = ('title', 'short_desc','body',)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.id})
    












    # def get(self,request):
    #     posts = Post.objects.all()
    #     return render(request,'index.html',{'posts':posts})

# class PostDetailView(View):
#     def get(self,request,pk):
#         post = get_object_or_404(Post,id=pk)
#         return render(request,'post.html',{'post': post})
    
# class PostDeleteView(View):
#     def delete(self,request,pk):
#         post = get_object_or_404(Post,id=pk)
#         post.delete()
#         return redirect('/posts')


# def posts(request):
#     posts = Post.objects.all()
#     return render(request,'index.html',{'posts':posts})

# def post(request,pk):
#     post = get_object_or_404(Post,id=pk)
#     return render(request,'post.html',{'post':post})

# def postdelete(request,pk):
#     post = get_object_or_404(Post,id=pk)
#     post.delete()
#     return redirect('/posts')

# def updatepost(request,pk):
#     post = get_object_or_404(Post,id=pk)
#     form = PostForm(initial={'title':post.title,"short_desc":post.short_desc,'body':post.body})
#     if request.method == 'POST':
#         form = PostForm(request.POST,instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('/posts')
#     return render(request,'update.html',{'form':form})
