## Lab2 Objectives:

- To enhance the product_module module to comply with the required ER Diagram.
- To enhance the brand and category modules to implement on product module.

---

## Introduction:

A module is a file with a . py extension that contains all the functions, classes and definitions pertaining to that module. A package is a collection of modules all saved inside a package folder.

## Procedures(Steps/Code):

1.  class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    In above section of code which is placed in models.py is creates a table to store a list of brand (i.e. with name variable), This also on active state.

2.  class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    class Meta:
    verbose_name_plural = "Categories"
    Similarly, thsi code is also run to craete Category tabel with name and on active status. Here teh Meta class is created to overwrite, use verbose_name_plural.

3.  class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500)
    color_code = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    registered_on = models.DateTimeField()
    is_active = models.BooleanField()
    Again, product table is created to store varoius details about product including brand and category table's foreign keys.

4.  python manage.py makemigrations
    python manage.py migrate

after creating any modules we need to perform makemigrations and migrate.

5.  from .models import Brand, Category, Product

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)

6.

- In browser, open 'http://127.0.0.1:8000'. This is the normal user mode
- In browser, open 'http://127.0.0.1:8000/admin' for admin interface
- Perform: create, read, update, delete operation for brand
- Perform: create, read, update, delete operation for category
- Perform: create, read, update, delete operation for product

---



---

## Conclusion:

I learned about the module a nd it's benefits
