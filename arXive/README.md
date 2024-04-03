# Esilv_Api_Project

This project involves creating an API that provides news related to Artificial Intelligence (AI). Our group has chosen the site Arxiv as our source of information.

### Objective

The objective of this project is to fetch information from the Arxiv site, either by scraping or through an existing API. We have created several endpoints for different purposes:

    - /get_data: Fetches a list of articles from the site. Retrieving 5 articles might be sufficient.
    - /articles: Displays information about the articles, including the article number, title, publication date, etc., but not the content itself.
    - /article/<number>: Accesses the content of a specified article.
    - /ml or /ml/<number>: Executes a machine learning script. Depending on the desired goal, it applies to either all articles or a single one. For example, sentiment analysis.

### Design

Our project uses FastAPI to create the API and BeautifulSoup for web scraping. We have also used the TextBlob library for sentiment analysis.

### Endpoints
Here's some screenshots and explannation for each API endpoints: 

/get_data

This endpoint returns a list of articles from the Arxiv site. The articles are retrieved using web scraping with BeautifulSoup. We have limited the number of articles to 5 for performance reasons.

Request:

    /get_data
    
Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/5159f2ce-d6f2-4248-a32d-dc9507f7bc84)


/articles

This endpoint returns a list of articles with information such as the article number, title, publication date, etc. The articles are retrieved using web scraping with BeautifulSoup.

Request:

    /articles

Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/3d93c65e-850d-412f-ba07-b20b15a5e440)


/article/<number>

This endpoint returns the content of a specified article. The content is retrieved using web scraping with BeautifulSoup.

Request:

    /article/{number of article}
    
Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/59910f1f-9dbd-47e9-a505-7b735554de47)


/ml or /ml/<number>

This endpoint executes a machine learning script to perform sentiment analysis on all articles or on a specified article. We have used the TextBlob library to perform sentiment analysis.

Request:

    /ml

Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/bffe0c2f-a650-4470-99f9-f67bd0907b89)



/ml/{number}

![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/4462c213-6f07-484a-a1f0-f074d4cf9c7e)

/get_categories
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/42db15b1-a14c-48bf-bad9-dcdbcd69e9a6)

/get_articles/math.CO
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/b4a26621-cff6-4faa-a5e1-3a1ea6dec2e9)

/categories/recent_articles
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/f2366280-dc10-4fb0-b36b-0a3acea3047d)


## Group Members

The members of the group are listed in the composition.txt file.

## Conclusion

