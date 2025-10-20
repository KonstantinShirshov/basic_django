from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError


forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите категорию продукта'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })

    def clean_name(self):
        product_name = self.cleaned_data.get('name')

        for word in forbidden_words:
            if word in product_name.lower():
                raise ValidationError('Вы используете запрещенные слова в названии продукта')
        return product_name

    def clean_description(self):
        product_description = self.cleaned_data.get('description')

        for word in forbidden_words:
            if word in product_description.lower():
                raise ValidationError('Вы используете запрещенные слова в описании продукта')
        return product_description

    def clean_price(self):
        product_price = self.cleaned_data.get('price')

        if product_price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return product_price
