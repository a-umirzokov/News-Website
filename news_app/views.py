from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .forms import ContactForm
from .models import News
# from django.shortcuts import get_object_or_404


class NewsListView(ListView):
    model = News
    queryset = News.published.all()
    template_name = 'news/news_list.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'blog'


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()
        context['news_list'] = News.published.all().order_by('-published_time')[:7]
        context['news_list1'] = News.published.all().order_by('published_time')[:7]
        context['lifestyle_news'] = News.published.all().order_by('-published_time').filter(category__name='LifeStyle')[:4]
        context['travel_news'] = News.published.all().order_by('-published_time').filter(category__name='Travel')[:4]
        context['health_news'] = News.published.all().order_by('-published_time').filter(category__name='Health')[:4]
        context['food_news'] = News.published.all().order_by('-published_time').filter(category__name='Food')[:4]
        context['sport_news'] = News.published.all().order_by('-published_time').filter(category__name='Sport')[:4]

        return context


def notfoundview(request):
    return render(request, 'news/page-404.html', status=404)


# def contactview(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         context = {
#             'form': form,
#             'success': True
#         }
#         return render(request, 'news/contact.html', context)
#     context = {
#         'form': form
#     }
#     return render(request, 'news/contact.html', context)


class NewsListView1(ListView):
    model = News
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['WorldNews'] = News.published.all().order_by('-published_time').filter(category__name='WorldNews')[:4]
        context['lifestyle_news'] = News.published.all().order_by('-published_time').filter(category__name='LifeStyle')[:4]
        return context


class ContactView(TemplateView):
    template_name = 'news/page-contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        context = {
            'form': form,
        }
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h2>Thank you for your message.</h2><a href="/contact">Go back to contact '
                                'page</a>')
        return render(request, self.template_name, context)


def blogauthorview(request):
    return render(request, 'news/blog-author.html')


def blogcategory1view(request):
    return render(request, 'news/blog-category-01.html')


def blogcategory2view(request):
    return render(request, 'news/blog-category-02.html')


def blogcategory3view(request):
    return render(request, 'news/blog-category-03.html')


def singleview(request):
    return render(request, 'news/single.html')


def singleaudioview(request):
    return render(request, 'news/single-audio.html')


def singlefullwidthview(request):
    return render(request, 'news/single-fullwidth.html')


def singlenomediaview(request):
    return render(request, 'news/single-no-media.html')


def singlevideoview(request):
    return render(request, 'news/single-video.html')


def singlesliderview(request):
    return render(request, 'news/single-slider.html')


def pageview(request):
    return render(request, 'news/page.html')


def pagefullwidth(request):
    return render(request, 'news/page-fullwidth.html')


def pagesitemap(request):
    return render(request, 'news/page-sitemap.html')


def pageskeleton(request):
    return render(request, 'news/page-skeleton.html')
