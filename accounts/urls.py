from django.urls import path

from accounts import views

urlpatterns = [
    path("", views.home, name="index"),
    path("about/", views.about, name="about"),
    path("feature/", views.feature, name="feature"),
    path("team/", views.team, name="team"),
    path("menu/", views.menu, name="menu"),
    path("booking/", views.booking, name="booking"),
    path("blog/", views.blog, name="blog"),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('add_comment/<slug:slug>/', views.add_comment, name="add_comment"),
]

