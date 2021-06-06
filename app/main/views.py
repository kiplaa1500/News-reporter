from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_all_news_sources, get_all_news_headlines, get_everything_news, get_business_headlines, search_articles


@main.route('/')
def index():
    """
    This function views the root page that returns index.html page
    and its data.
    """
    all_news_sources = get_all_news_sources()
    everything_news_items = get_everything_news()
    business_headliness = get_business_headlines()
    title = "Giko"
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search', source_name=search_article))
    else:
        return render_template("index.html", sources=all_news_sources, title=title, others=everything_news_items, business_headliness=business_headliness)


