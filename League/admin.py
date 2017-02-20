from django.contrib import admin
from .models import Comments,Article, Champion


class LeagueInline(admin.StackedInline):
    model = Comments
    extra = 1


class LeagueAdmin(admin.ModelAdmin):
    fields = ['title_article', 'title_text', 'data_time','champion']
    inlines = [LeagueInline]

class Champions(admin.ModelAdmin):
    fields = ['name', 'face']


admin.site.register(Article, LeagueAdmin)
admin.site.register(Champion, Champions)
