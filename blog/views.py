from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import NewCommentForm, PostSearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank



def home(request):
    all_posts = Post.newmanager.all()
    carousel_posts = Post.carouselmanager.all()
    return render(request, 'blog/index.html', {'posts' : all_posts, 'carousel_imgs' : carousel_posts})


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    
    # Heart likes
    fav = bool
    if post.favorites.filter(id=request.user.id).exists():
        fav = True
    # Heart likes
    
    allcomments = post.comments.filter(status=True)
    
    
    comment_form = NewCommentForm()
    
    return render(request, 'blog/single.html', {
        'post' : post, 
        'comment_form' : comment_form,
        'allcomments' : allcomments,
        'fav' : fav,
        })
    
def addcomment(request):
    
    if request.method == 'POST':
        
        if request.POST.get('action') == 'delete':
            id = request.POST.get('nodeid')
            c = Comment.objects.get(id=id)
            c.delete()
            return JsonResponse({'remove' : id})
        else:
            comment_form = NewCommentForm(request.POST)
        
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                user_comment.author = request.user
                user_comment.save()
                result = comment_form.cleaned_data.get('content')
                user = request.user.username
                return JsonResponse({'result' : result, 'user' : user})        
            

class CategoryListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'categorylist'
    
    def get_queryset(self):
        content = {
            'cat' : self.kwargs['category'],
            'posts' : Post.objects.filter(category__name=self.kwargs['category']).filter
            (status='published')
        }
        return content
    
    
def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        'category_list' : category_list,
    }
    return context
               
def post_search(request):
    form = PostSearchForm()
    q = ''
    results = []
     
    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            
            vector = SearchVector('title', weight='A') + \
                SearchVector('content', weight='A')
            query = SearchQuery(q)
            
            results = Post.objects.annotate(
                rank=SearchRank(vector, query, cover_density=True)).order_by('-rank')
                
            
            results = Post.objects.annotate(search=SearchVector(
                'title', 'content'),).filter(search=SearchQuery(q))
    
    return render(request, 'blog/search.html', {
        'form' : form,
        'q' : q,
        'results' : results,})
    
    