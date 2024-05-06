from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product

def index(request):
    return render(request, 'myapp/index.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product

def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        parent_id = request.POST.get('parent', None)
        parent = Category.objects.get(id=parent_id) if parent_id else None
        Category.objects.create(name=name, parent=parent)
        return redirect('category_list')
    return render(request, 'myapp/add_category.html')

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.name = request.POST['name']
        parent_id = request.POST.get('parent', None)
        category.parent = Category.objects.get(id=parent_id) if parent_id else None
        category.save()
        return redirect('category_list')
    return render(request, 'myapp/edit_category.html', {'category': category})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('category_list')

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        price = request.POST['price']
        Product.objects.create(name=name, category=category, price=price)
        return redirect('product_list')
    return render(request, 'myapp/add_product.html')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.category_id = request.POST['category']
        product.price = request.POST['price']
        product.save()
        return redirect('product_list')
    return render(request, 'myapp/edit_product.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')

from .models import Product

from .models import Category, Product

from .models import Category, Product

def index(request):
    # Fetch all products from the database
    products = Product.objects.all()

    # Fetch all category names from the database
    categories = Category.objects.all()

    # Pass the products and category names to the template
    return render(request, 'myapp/index.html', {'products': products, 'categories': categories})
