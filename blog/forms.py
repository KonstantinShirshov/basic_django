from django import forms
from blog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['created_at', 'views_counter']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название статьи'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите содержимое'
        })

        self.fields['preview'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['is_published'].widget.attrs.update({
            'class': 'custom-checkbox'
        })
