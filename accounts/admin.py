from django.contrib import admin
from .models import Staff, StaffImage, Category, ProductImage, Product, CategoryImage, BlogImage, Blog, Comment


class StaffImageInline(admin.TabularInline):
    model = StaffImage
    extra = 1

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("pk", "full_name", "job_title", "instagram")
    list_display_links = ("pk", "full_name", "job_title", "instagram")
    inlines = [StaffImageInline]

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CategoryImageInline]


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price",)
    list_display_links = ("pk", "title", "price")
    inlines = [ProductImageAdmin]


class BlogImageAdmin(admin.TabularInline):
    model = BlogImage
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "date")
    list_display_links = ("pk", "title", "slug", "date")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [BlogImageAdmin]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'content')
    list_display_links = ('pk', 'created', 'content')