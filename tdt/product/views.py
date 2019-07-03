from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm
from authentication.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string




def my_product_list(request):
    products = Product.objects.filter(users=request.user)
    return render(request, 'product_list.html', {'products': products, })

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('products:products_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('products:products_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products:products_list')



# class ProductCreateView(SuccessMessageMixin, FormView):
#     template_name = 'product_create.html'
#     initial = {}
#     form_class = ProductForm
#     success_url = '/thanks/'
#     success_message = 'success.'
#     data = dict()
#     def get(self, request, *args, **kwargs):
#         user_pk = request.user.pk
#         user1 = User.objects.get(pk = user_pk)
#         self.initial['username'] = user1
#         form = self.form_class(initial=self.initial)
#         self.data['html_form'] = render_to_string(self.template_name, {'form':form}, request=request)
#         return render(request, 'product_create.html', {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             if  request.user.is_authenticated:
#                 instance.user  = request.user
#             instance.save()
#             self.data['form_is_valid']=True
#             return JsonResponse(self.data)
#         else:
#             self.data['form_is_valid']=False
#             self.data['html_form'] = render_to_string(self.template_name, {'form':form}, request=request)
#         return render(request, 'product_create.html', {'form': form})
