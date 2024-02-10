from django.urls import path
from news_app import views as v

urlpatterns = [
    path('', v.HomePageView.as_view(), name='home'),  # This is the home page (news_app/views.py)
    path('news', v.NewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>/', v.NewsDetailView.as_view(), name='news_detail'),
    path('404', v.notfoundview, name='page-404'),
    path('contact', v.ContactView.as_view(), name='page-contact'),
    path('blog-author', v.blogauthorview, name='blog-author'),
    path('blog-category-01', v.BlogCategory1view.as_view(), name='blog-category-01'),
    path('blog-category-02', v.blogcategory2view, name='blog-category-02'),
    path('blog-category-03', v.blogcategory3view, name='blog-category-03'),
    path('single', v.singleview, name='single'),
    path('single-audio', v.singleaudioview, name='single-audio'),
    path('single-fullwidth', v.singlefullwidthview, name='single-fullwidth'),
    path('single-no-media', v.singlenomediaview, name='single-no-media'),
    path('single-slider', v.singlesliderview, name='single-slider'),
    path('single-video', v.singlevideoview, name='single-video'),
    path('page', v.pageview, name='page'),
    path('page-fullwidth', v.pagefullwidth, name='page-fullwidth'),
    path('page-sitemap', v.pagesitemap, name='page-sitemap'),
    path('page-skeleton', v.pageskeleton, name='page-skeleton'),
]
