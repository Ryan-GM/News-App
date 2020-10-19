from app import app
import urllib.request,json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_result = None

        if get_news_response['result']:
            news_result_list = get_news_response['result']
            news_result = process_result(news_result_list)

    return news_result

def process_result(news_list):
    '''
    Function to process the news results and return a list of objects

    Args:
        news_list: List of dictionaries containing news' details

    Returns:
         news_results: List of movie objects
    '''
    news_result = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        overview = news_item.get('overview')
        poster = news_item.get('poster_path')
        vote_count = news_item.get('vote_count')

        if poster:
            news_object = News(id,title,overview,poster,vote_count)
            news_result.append(news_object)

    return news_result