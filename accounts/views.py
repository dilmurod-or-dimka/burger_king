from audioop import reverse

from django.core.exceptions import BadRequest
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from .utils import send_to_telegram, send_email_for_contact_us
from .models import Staff, Category, Blog, Comment
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib import messages as django_messages


def home(request):
    staffs = Staff.objects.all()
    blogs = Blog.objects.all()[:2]
    categories = Category.objects.all()
    context = {
        'staffs': staffs,
        'categories': categories,
        'blogs': blogs,
        'active': 'home'
    }

    return render(request, 'pages/index.html', context)


def about(request):
    context = {
        'active': 'about'
    }
    return render(request, 'pages/about.html', context)


def feature(request):
    context = {
        'active': 'feature'
    }
    return render(request, 'pages/feature.html', context)


def team(request):
    staffs = Staff.objects.all()
    context = {
        'staffs': staffs,
        'active': 'team'
    }
    return render(request, 'pages/team.html', context)


def menu(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'active': 'menu'
    }
    return render(request, 'pages/menu.html', context)


def booking(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        user_name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        time = request.POST.get('time')

        if not all([user_name, email, mobile, date, time]):
            return HttpResponse("Please fill all the fields.")

        body = {
            'user_name': user_name,
            'email': email,
            'mobile': mobile,
            'date': date,
            'time': time,
        }
        messages = "\n".join(body.values())

        try:
            send_to_telegram(messages)
            django_messages.success(request, "Your booking has been sent.")
        except BadRequest as e:
            print(f"Error sending message: {str(e)}")
            return HttpResponse("Please try again.")
        return redirect("index")
    context = {
        'categories': categories,
        'active': 'booking',
    }

    return render(request, 'pages/booking.html', context)


def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    context = {
        'blogs': blogs,
        'active': 'blog'
    }
    return render(request, 'pages/blog.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blogs = Blog.objects.all()
    blog_date = Blog.objects.all().order_by('-date')
    comments = Comment.objects.filter(blog=blog)

    context = {
        'blog': blog,
        'blogs': blogs,
        'blog_date': blog_date,
        'comments': comments,
    }
    return render(request, 'pages/blog_detail.html', context)


def contact(request):
    context = {
        'active': 'pages',
    }
    if request.method == 'POST':
        user_name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_email_for_contact_us(user_name, subject, message, email)

        return HttpResponseRedirect('/contact/')

    return render(request, 'pages/contact.html', context)


def add_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    user_name = request.POST.get('user_name')
    email = request.POST.get('email')
    content = request.POST.get('content')

    comment = Comment(blog=blog, user_name=user_name, email=email, content=content)
    comment.save()
    return redirect('blog_detail', slug=slug)
