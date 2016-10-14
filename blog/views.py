from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostearForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def detalle_articulo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_articulo.html', {'post': post})

def postear_nuevo(request):
    if request.method == "POST":
        formulario = PostearForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.detalle_articulo', pk=post.pk)
    else:
        formulario = PostearForm()
    return render(request, 'blog/postear_articulo.html', {'formulario': formulario})

def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        formulario = PostearForm(request.POST, instance=post)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.detalle_articulo', pk=post.pk)
    else:
        formulario = PostearForm(instance=post)
    return render(request, 'blog/postear_articulo.html', {'formulario': formulario})
