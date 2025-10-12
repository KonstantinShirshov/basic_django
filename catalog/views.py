from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, FormView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'


class ProductTemplateView(TemplateView):
    model = Product
    template_name = 'contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ContactFormView(FormView):
    template_name = 'contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        # Другие действия с данными формы
        return HttpResponse(f'Спасибо, {name}! Мы с вами свяжемся в ближайшее время.')


# def answer(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#
#         return HttpResponse(f'Спасибо, {name}! Мы с вами свяжемся в ближайшее время.')
#     return render(request, 'contacts.html')
