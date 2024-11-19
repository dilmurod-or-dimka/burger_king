from xml.dom.minidom import Comment

from django.db import models
from django.urls import reverse

class Staff(models.Model):
    full_name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    facebook = models.URLField(verbose_name="Facebook", blank=True, null=True)
    twitter = models.URLField(verbose_name="Twitter", blank=True, null=True)
    instagram = models.URLField(verbose_name="Instagram", blank=True, null=True)
    linkedin = models.URLField(verbose_name="LinkedIn", blank=True, null=True)

    def __str__(self):
        return self.full_name

    def get_photo_staff(self):
        photo = self.staffimage_set.all().first()
        if photo is not None:
            return photo.photo.url
        return None

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

class StaffImage(models.Model):
    photo = models.ImageField(verbose_name="Photo", upload_to="staff/", blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, null=True)

    def get_absolute_url(self):
        return reverse("menu", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slug = self.slug
            num = 1
            while Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{num}"
                num += 1
            self.slug = unique_slug
        return super().save(*args, **kwargs)

    def get_first_photo(self):
        photo = self.categoryimage_set.first()
        if photo:
            return photo.photo.url
        return "https://cs8.pikabu.ru/post_img/big/2016/09/10/4/1473482891145853538.jpg"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class CategoryImage(models.Model):
    photo = models.ImageField(verbose_name="Photo", upload_to="products/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_first_photo(self):
        photo = self.productimage_set.first()
        if photo:
            return photo.photo.url
        return "https://cs8.pikabu.ru/post_img/big/2016/09/10/4/1473482891145853538.jpg"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class ProductImage(models.Model):
    photo = models.ImageField(verbose_name="Photo", upload_to="products/", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    slug = models.SlugField(max_length=150, unique=True, null=True)

    def __str__(self):
        return self.title

    def get_first_photo(self):
        photo = self.blogimage_set.first()
        if photo:
            return photo.photo.url
        return "https://cs8.pikabu.ru/post_img/big/2016/09/10/4/1473482891145853538.jpg"

class BlogImage(models.Model):
    photo = models.ImageField(verbose_name="Photo", upload_to="blog/", blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.blog.title}"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=150)
    content = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}: {self.email}"