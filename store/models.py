from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse
from django.conf import settings

# Creating functions for models
def image_folder(instanse, fileName):
    fileName = instanse.slug + '.' + fileName.split('.')[1]
    return "{0}/{1}".format(instanse.slug, fileName)


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ParentCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to= image_folder, blank=True, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('parent_category_detail', kwargs={'parent_category_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    parentCategory = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, default=None, db_index=True)
    image = models.ImageField(upload_to=image_folder, blank=True, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class MoneyType(models.Model):
    name = models.CharField(max_length=10)
    exchangeRate = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    description = models.TextField(default='НАПИШИТЕ ОПИСАНИЕ ПРОДУКТА!', blank=True)
    # image = models.ImageField(upload_to=image_folder, blank=True, default=None)
    warranty = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    money = models.ForeignKey(MoneyType, on_delete=models.CASCADE,)

    avaliable = models.BooleanField(default=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_final_price(self):
        return int(self.price * self.money.exchangeRate)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})





class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return "Cart Item for product {0}".format(self.product.name)


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return str(self.id)

    def add_to_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, item_total_price=product.price)
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()

    def remove_from_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()

    def change_quantity(self, quantity, item_id):
        cart_item = CartItem.objects.get(id=int(item_id))
        cart = self
        cart_item.quantity = int(quantity)
        cart_item.item_total_price = int(quantity) * Decimal(cart_item.product.price)
        cart_item.save()
        new_cart_total = 0.00
        for item in cart.items.all():
            new_cart_total += float(item.item_total_price)
        cart.cart_total_price = new_cart_total
        cart.save()


ORDER_STATUS_CHOICES = (
    ('Принят в обработку', 'Принят в обработку'),
    ('Выполнен', 'Выполнен')
)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=225, blank=True)
    buying_type = models.CharField(max_length=40, choices=(('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')), default='Самовывоз')
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True)
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])

    def __str__(self):
        return "Заказ № {0}".format(str(self.id))

    def detail(self):
        return "заказа № {0}".format(str(self.id))


def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=ParentCategory)
pre_save.connect(pre_save_category_slug, sender=Category)
pre_save.connect(pre_save_category_slug, sender=Product)






