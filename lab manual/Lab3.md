## Objectives

- To add searching capability in the admin dashboard for products, categories, and brands

---

## Introduction

A common task for web applications is to search some data in the database with user input. In a simple case, this could be filtering a list of objects by a category. A more complex use case might require searching with weighting, categorization, highlighting, multiple languages, and so on.

In this lab, we adding seaching capabilities in the admin panel to find or filter the desired product, brand, or category. This would help finding the right object when querying through a list of records in the database.

---

## Procedure

1.  Enhance the admin for search enhancements. Open “admin.py”.

    Replace

        admin.site.register(Product)

    with

        class ProductAdmin(admin.ModelAdmin):
            list_display = ["name", "price", "brand", "category",]
            search_fields = ["name", "price", "brand__name", "category__name",]
            list_filter = ["brand","category",]
            readonly_fields = ["quantity",]

            class Meta:
                model = Product

        admin.site.register(Product, ProductAdmin)

2.  Make similar changes to other models, e.g. Brand, Category, etc.

3.  Run the project and navigate to admin

4.  To display image in list view, first add a field “image_tag” to Product class in
    ‘models.py’.

            ...
            from django.utils.html import mark_safe
            ...
            class Product(models.Model):
                ...

                def image_tag(self):
                    return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')

            image_tag.short_description = "Product"

            def __str__(self):
                    return self.name

5.  Let’s display image to list view. Go to 'admin.py' and modify the ProductAdmin as
    below:

            ...
            class ProductAdmin(admin.ModelAdmin):
            list_display = ["image_tag", "name", "price", "brand", "category",]
            search_fields = ["name", "price", "brand__name", "category__name",]
            list_filter = ["brand","category","price",]
            # readonly_fields = ["quantity",]
            class Meta:
            model = Product
            admin.site.register(Product, ProductAdmin)

6.  Run the project and navigate to admin to check the result.

---


## Conclusion

I learned how to designed & develop code to search product in django.
