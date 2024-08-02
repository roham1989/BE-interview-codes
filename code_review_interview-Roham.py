# 1
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# 2
def GetThirdElement(numbers):
    return numbers[2]

# 3
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

# 4
def greet(name):
    return "Hello, %s!" % name

# 5
def check_greeting(greeting):
    if greeting is "hello":
        return True
    return False

# 6

class A:
    def do_something(self):
        return "Doing something in A"

class B(A):
    def do_something(self):
        return "Doing something in B"

class C(A):
    def do_something(self):
        return "Doing something in C"

class D(B, C):
    pass

# Test case
d = D()
print(d.do_something())

# 7
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        return 3.14 * (4**2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_side(self):
        return self.side


# 8
class MathOperations:

    def multiply(self, a, b):
        return a * b

# ============================ Django and DRF ========================== #

# 9
def get_active_products():
    products = Product.objects.all()
    active_product_names = [product.name for product in products if product.is_active]
    return active_product_names

# 10
def get_customer_count():
    customers = Customer.objects.all()
    return len(customers)

# 11
def has_active_users():
    users = User.objects.filter(is_active=True)
    return len(users) > 0

# 12
def get_total_sales():
    sales = Sale.objects.all()
    total = sum(sale.amount for sale in sales)
    return total

# 13
def update_all_products():
    for product in Product.objects.all():
        product.is_active = True
        product.save()

# 14
def update_customer_with_lock():
    # Knowing select related is a must for answering this question
    with transaction.atomic():
        for customer in Customer.objects.select_related('user').select_for_update():
            if customer.user.is_active:
                customer.is_active = True
                customer.save()

# 15
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 16
class CustomPagination(PageNumberPagination):
    page_size = 10

class ProductListView(APIView):
    pagination_class = CustomPagination

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# 17
def update_products():
    inactive_products = Product.objects.filter(is_active=False)
    Product.objects.filter(is_active=False).update(is_active=True)
    return inactive_products.count()

# 18
class blog_metadata(models.Model):
    title_of_the_blog = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    content_body = models.JSONField(default=dict())


# Bonus Question
class Test:
    @lru_cache
    def get_last_year_products_total_price(self):
        last_year = datetime.now().year - datetime.timedelta(days=365)
        return Product.objects.filter(created_at__lt=last_year).aggregate(total=Sum("product_price"))
