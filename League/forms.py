from django.forms import ModelForm
from .models import Comments,Article,Champion


class CommentForm(ModelForm):
    class Meta:
         model = Comments
         fields = ['comments_text']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title_article', 'title_text','champion','data_time']
