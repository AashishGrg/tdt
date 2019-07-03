from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    # username = forms.CharField(max_length=20, widget=forms.TextInput(
    #     attrs={'readonly': 'readonly'}))
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('username','product_name','product_type','status','detail','product_image','price','quantity')


