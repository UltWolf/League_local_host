from django.shortcuts import render
from django.http.response import HttpResponse, Http404

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response,redirect
from League.models import Article, Comments,Champion
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.template.context_processors import csrf
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import auth


def index(request):
    return render_to_response('index.html', {'username': auth.get_user(request).username})


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all(), 'Champions': Champion.objects.all(), 'username': auth.get_user(request).username})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/articles/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/articles/')
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/articles/')


def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)


class ArticleCreate(CreateView):
    model = Article
    fields = ['title_article', 'author', 'title_text', 'data_time', 'champion_name' ]


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title_article', 'author', 'title_text', 'data_time', ]


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('League:index')


