from django.contrib import admin
from models import Comments,Article


class LeagueInline(admin.StackedInline):
    model = Comments
    extra = 1


class LeagueAdmin(admin.ModelAdmin):
    fields = ['title_article', 'author', 'data_time']
    inlines = [LeagueInline]
admin.site.register(Article, LeagueAdmin)
