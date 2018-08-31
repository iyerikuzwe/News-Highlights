from app import app
import urllib.request,json
from .models import topnews, catnews

Topnews = topnews.Topnews
Catnews = catnews.Catnews

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting top news base url
base_url = app.config["TOPNEWS_API_BASE_URL"]
base2_url = app.config["CATEGORIES_API_BASE_URL"]

def get_topnews(source):
    """
    Function that gets the json response to our url request
    """
    get_topnews_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_topnews_url) as url:
        get_topnews_data = url.read()
        get_topnews_response = json.loads(get_topnews_data)
        print(get_topnews_response)
        topnews_results = None

        if get_topnews_response['articles']:
            topnews_results_list = get_topnews_response['articles']
            topnews_results = process_results(topnews_results_list)

    return topnews_results

def process_results(topnews_list):
    '''
    Function  that processes the topnews result and transform them to a list of Objects

    Args:
        topnews_list: A list of dictionaries that contain topnews details

    Returns :
        topnews_results: A list of topnews objects
    '''
    topnews_results = []
    for topnews_item in topnews_list:
        name = topnews_item.get('name')
        title = topnews_item.get('title')
        author = topnews_item.get('author')
        description = topnews_item.get('description')
        urlToImage = topnews_item.get('urlToImage')
        url = topnews_item.get('url')

        if urlToImage:
            topnews_object = Topnews(name,author,title,description,urlToImage,url)
            topnews_results.append(topnews_object)

    return topnews_results



def get_catnews(category):
    """
    Function that gets the json response to our url request
    """
    get_catnews_url = base2_url.format(category,api_key)

    with urllib.request.urlopen(get_catnews_url) as url:
        get_catnews_data = url.read()
        get_catnews_response = json.loads(get_catnews_data)
        print(get_catnews_response)
        catnews_results = None

        if get_catnews_response['sources']:
            catnews_results_list = get_catnews_response['sources']
            catnews_results = process2_results(catnews_results_list)

    return catnews_results

def process2_results(catnews_list):
    '''
    Function  that processes the catnews result and transform them to a list of Objects

    Args:
        catnews_lis A list of dictionaries that contain catnews details
t:
    Returns :
        catnews_results: A list of catnews objects
    '''
    catnews_results = []
    for catnews_item in catnews_list:
        id = catnews_item.get('id')
        name = catnews_item.get('name')
        description = catnews_item.get('description')
        url = catnews_item.get('url')

        if id:
            catnews_object = Catnews(id,name,description,url)
            catnews_results.append(catnews_object)

    return catnews_results
