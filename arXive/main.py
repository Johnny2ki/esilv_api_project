
from fastapi import FastAPI, HTTPException
from textblob import TextBlob
import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup

# Creation of API
app = FastAPI()

@app.get("/get_data")
async def get_all_info():
    url = "https://export.arxiv.org/list/cs.AI/recent"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for dt in soup.find_all('dt'):
            # Initialize a dictionary to hold article info
            article_info = {}

            # Find the anchor tag containing the abstract link
            a_tag = dt.find('a', title="Abstract")
            if a_tag and 'href' in a_tag.attrs:
                article_id = a_tag['href'].split('/')[-1]
                article_info['article_id'] = article_id
            else:
                continue  # Skip this article if the ID cannot be determined

            # The corresponding 'dd' tag contains title, authors, and other info
            dd = dt.find_next_sibling('dd')
            if dd:
                # Extract title
                title_div = dd.find('div', class_='list-title mathjax')
                if title_div:
                    title = title_div.text.replace('Title:', '').strip()
                    article_info['title'] = title
                
                # Extract authors
                authors_div = dd.find('div', class_='list-authors')
                if authors_div:
                    authors = authors_div.text.replace('Authors:', '').replace('\n', '').strip()
                    article_info['authors'] = authors
                
                # Extract abstract URL
                abstract_url = "https://arxiv.org" + a_tag.get('href')
                article_info['abstract_url'] = abstract_url
            
            # Add the article's info to the articles list, if we have a title
            if 'title' in article_info:
                articles.append(article_info)

        return {"articles": articles}
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from the arXiv page")
    
### get the list of articles ###
@app.get("/articles")
async def get_data():
    url = "https://export.arxiv.org/list/cs.AI/recent"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for dt in soup.find_all('dt'):
            # Initialize a dictionary to hold article info
            article_info = {}

            # Find the anchor tag containing the abstract link, which includes the article ID
            a_tag = dt.find('a', title="Abstract")
            if a_tag:
                article_id = a_tag['href'].split('/')[-1]
                article_info['article_id'] = article_id

            # The corresponding 'dd' tag contains title, authors, and other info
            dd = dt.find_next_sibling('dd')
            if dd:
                # Extract title
                title_div = dd.find('div', class_='list-title mathjax')
                if title_div:
                    title = title_div.text.replace('Title:', '').strip()
                    article_info['title'] = title
                
                # Extract authors
                authors_div = dd.find('div', class_='list-authors')
                if authors_div:
                    authors = authors_div.text.replace('Authors:', '').replace('\n', '').strip()
                    article_info['authors'] = authors
                
                # Publication date is not directly listed on this page, so this might need to be inferred or omitted
                # If you have a specific way to determine the publication date, you can add it here
                # For now, we'll skip adding the publication date due to the lack of direct availability in this context
            
            # Add the article's info to the articles list
            articles.append(article_info)

        return articles
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from the arXiv page")


### get articles info  ###
@app.get("/article/{arxiv_id}")
async def scrape_article(arxiv_id: str):
    # Construct the URL to the specific arXiv page using the arXiv ID
    url = f"https://arxiv.org/abs/{arxiv_id}"

    # Make the HTTP GET request to the arXiv page
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find elements by their HTML tags and attributes
        # This is based on the common structure of arXiv pages
        # You need to adjust the selectors based on the actual HTML structure of arXiv article pages
        title = soup.find('h1', class_='title').text.replace("Title:", "").strip()
        authors = [author.text for author in soup.find_all('a', rel='author')]
        abstract = soup.find('blockquote', class_='abstract').text.replace("Abstract:", "").strip()

        # Return the extracted information
        return {
            "title": title,
            "authors": authors,
            "summary": abstract
        }
    else:
        # If the response status code is not 200, raise an HTTPException
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch the page from arXiv")

# To use this endpoint, you would need to start the FastAPI server and make a GET request to
# /scrape-article/{arxiv_id}, where {arxiv_id} is the arXiv ID of the paper.
    
ARXIV_API_URL = "http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&start=0&max_results=5"


def fetch_ai_articles():
    # Make the HTTP GET request to the ArXiv API
    response = requests.get(ARXIV_API_URL)
    
    if response.status_code == 200:
        # Parse the XML response
        root = ElementTree.fromstring(response.content)
        
        # Initialize a list to hold the article data
        articles_data = []
        
        # Extract article data
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            article_data = {
                'id': entry.find('{http://www.w3.org/2005/Atom}id').text.strip(),
                'title': entry.find('{http://www.w3.org/2005/Atom}title').text.strip(),
                'summary': entry.find('{http://www.w3.org/2005/Atom}summary').text.strip(),
            }
            articles_data.append(article_data)
        
        return articles_data
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch data from the ArXiv API")

def analyze_sentiment_all_articles():
    articles = fetch_ai_articles()
    sentiments = []
    for article in articles:
        blob = TextBlob(article['summary'])
        sentiment = blob.sentiment
        sentiments.append({
            'article_id': article['id'],
            'sentiment_polarity': sentiment.polarity,
            'sentiment_subjectivity': sentiment.subjectivity
        })    
    return sentiments

def analyze_sentiment_single_article(article_id):
    ARXIV_SINGLE_API_URL = f"http://export.arxiv.org/api/query?id_list={article_id}"
    response = requests.get(ARXIV_SINGLE_API_URL)
    
    if response.status_code == 200:
        # Parse the XML response for the single article
        root = ElementTree.fromstring(response.content)
        entry = root.find('{http://www.w3.org/2005/Atom}entry')
        if entry:
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
            blob = TextBlob(summary)
            sentiment = blob.sentiment
            return {
                'article_id': article_id,
                'sentiment_polarity': sentiment.polarity,
                'sentiment_subjectivity': sentiment.subjectivity
            }
                    
        else:
            raise HTTPException(status_code=404, detail="Article not found.")
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch data from the ArXiv API")

## endpoint ml and ml/articles

@app.get("/ml", tags=["ml"])
def analyze_sentiment_all():
    return analyze_sentiment_all_articles()

@app.get("/ml/{article_number}", tags=["ml"])
def analyze_sentiment_single(article_number: str):
    return analyze_sentiment_single_article(article_number)


# Fetch differents categories of article available on arXiv
@app.get("/get_categories")
def get_categories():
    # Predefined list of categories based on arXiv's subject classifications
    categories = {
        'cs.AI': 'Artificial Intelligence',
        'cs.LG': 'Machine Learning',
        'math.CO': 'Combinatorics',
        'physics.optics': 'Optics',
        'econ.EM': 'Econometrics',
        # Add more categories as needed
    }
    return categories


# Give the recent articles  with their ids accoridng to the categories 
@app.get("/recent_articles/{category}")
def fetch_recent_articles_by_category(category: str, max_results: int = 10):
    arxiv_api_url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results={max_results}"
    response = requests.get(arxiv_api_url)
    
    if response.status_code == 200:
        root = ElementTree.fromstring(response.content)
        articles = [
            {
                'id': entry.find('{http://www.w3.org/2005/Atom}id').text.strip(),
                'title': entry.find('{http://www.w3.org/2005/Atom}title').text.strip(),
            }
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry')
        ]
        return articles
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch data from the arXiv API")
    

from typing import List, Dict

# Assuming this is a predefined list of categories you're interested in
INTERESTED_CATEGORIES = ['cs.AI', 'cs.LG', 'math.CO', 'physics.optics', 'econ.EM']

# Fetch all recent articles and details of their categories
def fetch_recent_articles_from_category(category: str, max_results: int = 5) -> List[Dict]:
    arxiv_api_url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results={max_results}"
    response = requests.get(arxiv_api_url)
    
    if response.status_code == 200:
        root = ElementTree.fromstring(response.content)
        articles = [
            {
                'id': entry.find('{http://www.w3.org/2005/Atom}id').text.strip(),
                'title': entry.find('{http://www.w3.org/2005/Atom}title').text.strip(),
            }
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry')
        ]
        return articles
    else:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data from the arXiv API for category {category}")

@app.get("/categories/recent_articles")
def get_categories_recent_articles(max_results: int = 5):
    categories_recent_articles = {}
    for category in INTERESTED_CATEGORIES:
        categories_recent_articles[category] = fetch_recent_articles_from_category(category, max_results)
    return categories_recent_articles
