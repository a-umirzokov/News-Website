from .models import News


def latest_news(request):
    latest_news = News.published.all().order_by('-published_time')[:3]
    health_news = News.published.all().order_by('-published_time').filter(category__name='Health')[:4]
    context = {
        'latest_news': latest_news,
        'health_news': health_news
    }
    return context
