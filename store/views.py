from django.shortcuts import render, reverse
from store.models import *
from django.http import HttpResponseRedirect, JsonResponse
from decimal import Decimal
from store.forms import OrderForm, RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def main_view(request):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all()
    login_my = LoginForm(request.POST or None)
    if login_my.is_valid():
        username = login_my.cleaned_data['username']
        password = login_my.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))

    register = RegistrationForm(request.POST or None)
    if register.is_valid():
        new_user = register.save(commit=False)
        username = login_my.cleaned_data['username']
        email = register.cleaned_data['email']
        password = register.cleaned_data['password']
        first_name = register.cleaned_data['first_name']
        last_name = register.cleaned_data['last_name']
        new_user.email = email
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart,
        'register': register,
        'login_my': login_my
    }
    return render(request, 'main.html', context)


def product_view(request, product_slug):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all()
    login_my = LoginForm(request.POST or None)
    if login_my.is_valid():
        username = login_my.cleaned_data['username']
        password = login_my.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))

    register = RegistrationForm(request.POST or None)
    if register.is_valid():
        new_user = register.save(commit=False)
        username = login_my.cleaned_data['username']
        email = register.cleaned_data['email']
        password = register.cleaned_data['password']
        first_name = register.cleaned_data['first_name']
        last_name = register.cleaned_data['last_name']
        new_user.email = email
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart,
        'register': register,
        'login_my': login_my,
    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all()
    login_my = LoginForm(request.POST or None)
    if login_my.is_valid():
        username = login_my.cleaned_data['username']
        password = login_my.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))

    register = RegistrationForm(request.POST or None)
    if register.is_valid():
        new_user = register.save(commit=False)
        username = login_my.cleaned_data['username']
        email = register.cleaned_data['email']
        password = register.cleaned_data['password']
        first_name = register.cleaned_data['first_name']
        last_name = register.cleaned_data['last_name']
        new_user.email = email
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category, avaliable=True)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart,
        'register': register,
        'login_my': login_my,
    }
    return render(request, 'category.html', context)


def parent_category_view(request, parent_category_slug):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all()
    login_my = LoginForm(request.POST or None)
    if login_my.is_valid():
        username = login_my.cleaned_data['username']
        password = login_my.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))

    register = RegistrationForm(request.POST or None)
    if register.is_valid():
        new_user = register.save(commit=False)
        username = login_my.cleaned_data['username']
        email = register.cleaned_data['email']
        password = register.cleaned_data['password']
        first_name = register.cleaned_data['first_name']
        last_name = register.cleaned_data['last_name']
        new_user.email = email
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    try:
        parrentCategory = ParentCategory.objects.get(slug=parent_category_slug)
    except ParentCategory.DoesNotExist:
        parrentCategory = ParentCategory.objects.all()

    context = {
        'parrentCategories': parrentCategories,
        'categories': categories,
        'parrentCategory': parrentCategory,
        'cart': cart,
        'register': register,
        'login_my': login_my
    }
    return render(request, 'parrentCategory.html', context)


def cart_view(request):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all()
    login_my = LoginForm(request.POST or None)
    if login_my.is_valid():
        username = login_my.cleaned_data['username']
        password = login_my.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))

    register = RegistrationForm(request.POST or None)
    if register.is_valid():
        new_user = register.save(commit=False)
        username = login_my.cleaned_data['username']
        email = register.cleaned_data['email']
        password = register.cleaned_data['password']
        first_name = register.cleaned_data['first_name']
        last_name = register.cleaned_data['last_name']
        new_user.email = email
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context ={
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart,
        'register': register,
        'login_my': login_my
    }
    return render(request, 'cart.html', context)


def checkout_view(request):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all()
    login_my = LoginForm(request.POST or None)
    if login_my.is_valid():
        username = login_my.cleaned_data['username']
        password = login_my.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))

    register = RegistrationForm(request.POST or None)
    if register.is_valid():
        new_user = register.save(commit=False)
        username = login_my.cleaned_data['username']
        email = register.cleaned_data['email']
        password = register.cleaned_data['password']
        first_name = register.cleaned_data['first_name']
        last_name = register.cleaned_data['last_name']
        new_user.email = email
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    form = OrderForm(request.POST or None)

    context = {
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart,
        "form": form,
        'register': register,
        'login_my': login_my,
    }
    return render(request, 'checkout.html', context)


def account_view(request):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all()
    order = Order.objects.filter(user=request.user)
    order_active = order.filter(status='Принят в обработку').order_by('-id')
    order_finished = order.filter(status='Выполнен').order_by('-id')
    login_my = LoginForm(request.POST or None)
    if login_my.is_valid():
        username = login_my.cleaned_data['username']
        password = login_my.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))

    register = RegistrationForm(request.POST or None)
    if register.is_valid():
        new_user = register.save(commit=False)
        username = login_my.cleaned_data['username']
        email = register.cleaned_data['email']
        password = register.cleaned_data['password']
        first_name = register.cleaned_data['first_name']
        last_name = register.cleaned_data['last_name']
        new_user.email = email
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    conetext = {
        'order': order,
        'parrentCategories': parrentCategories,
        'categories': categories,
        'register': register,
        'login_my': login_my,
        'order_active': order_active,
        'order_finished': order_finished
    }
    return render(request, 'account.html', conetext)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))


def make_order_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        name = request.user.first_name
        last_name = request.user.last_name
        phone = form.cleaned_data['phone']
        buying_type = form.cleaned_data['buying_type']
        address = form.cleaned_data['address']
        comments = form.cleaned_data['comments']
        new_order = Order.objects.create(
            user=request.user,
            items=cart,
            total=cart.cart_total_price,
            first_name=name,
            last_name=last_name,
            phone=phone,
            address=address,
            buying_type=buying_type,
            comments=comments)
        del request.session['cart_id']
        del request.session['total']
        return HttpResponseRedirect(reverse('account'))
    elif not form.is_valid():
        name = request.user.first_name
        last_name = request.user.last_name
        phone = form.cleaned_data['phone']
        buying_type = form.cleaned_data['buying_type']
        address = form.cleaned_data['address']
        comments = form.cleaned_data['comments']
        new_order = Order.objects.create(
            user=request.user,
            items=cart,
            total=cart.cart_total_price,
            first_name=name,
            last_name=last_name,
            phone=phone,
            address=address,
            buying_type=buying_type,
            comments=comments)
        del request.session['cart_id']
        del request.session['total']
        return HttpResponseRedirect(reverse('account'))


def add_to_cart_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total_price)
    cart.cart_total_price = new_cart_total
    cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'cart_total_price': cart.cart_total_price})


def remove_from_cart_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.remove_from_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total_price)
    cart.cart_total_price = new_cart_total
    cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'cart_total_price': cart.cart_total_price})


def change_item_quantity(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
    quantity = request.GET.get('quantity')
    item_id = request.GET.get('item_id')
    cart_item = CartItem.objects.get(id=int(item_id))
    cart_item.quantity = int(quantity)
    cart_item.item_total_price = int(quantity) * Decimal(cart_item.product.price)
    cart_item.save()
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total_price)
    cart.cart_total_price = new_cart_total
    cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'item_total_price': cart_item.item_total_price,
        'cart_total_price': cart.cart_total_price
    })
