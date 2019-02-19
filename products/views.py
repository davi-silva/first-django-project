from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=10)
    my_context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", my_context)

# Create a form view
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    my_context = {
        'form': form
    }
    return render(request, "products/product_create.html", my_context)

# def product_create_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     my_context = {}
#     return render(request, "products/product_create.html", my_context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # new the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     my_context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", my_context)



