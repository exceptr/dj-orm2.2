from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        basic = []
        for form in self.forms:
            for v in form.cleaned_data.values():
                if v == bool(True):
                    basic.append(v)
                    if len(basic) > 1:
                        raise ValidationError('Выберите одну основную категорию')
                elif v == bool(False):
                    if len(basic) == 0:
                        raise ValidationError('Выберите основную категорию')

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 1
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['title', 'published_at']
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
