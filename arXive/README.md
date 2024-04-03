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

## /get_data

This endpoint returns a list of articles from the Arxiv site. The articles are retrieved using web scraping with BeautifulSoup. We have limited the number of articles to 5 for performance reasons.

To get a list of articles, send a GET request to http://localhost:8000/get_data. This will return a JSON object containing information about the latest articles in the AI category.

Request:

    GET request to http://localhost:8000/get_data
    
Response:

    {"articles": [{"article_id": "2403.20306", "title": "Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference", "authors":"Jovan Stojkovic, Esha Choukse, Chaojie Zhang, Inigo Goiri, Josep Torrellas", "abstract_url":"https://arxiv.org/abs/2403.20306"},{"article_id": "2403.20234","title":"Artificial Neural Networks-
    based Real-time Classification of ENG Signals for Implanted Nerve Interfaces", "authors":"ntonio Coviello , Francesco Linsalata, Umberto Spagnolini, Maurizio Magarini", "abstract_url":"https://arxiv.org/abs/2403.20234"}, {"article_id": "2403.20212", "title": "On Size and Hardness Generalization in Unsupervised Learning for the
    Travelling Salesman Problem", "authors"; "Yimeng Min, Carla P. Gomes", "abstract_url":"https://arxiv.org/abs/2403.20212"},{"article_id": "2403.20204","title":"The Future of
    Combating Rumors? Retrieval, Discrimination, and Generation", "authors":"Junhao Xu, Longdi Xian, Zening Liu, Mingliang Chen, Qiuyang Yin, Fenghua
    Song", "abstract_url":"https://arxiv.org/abs/2403.20204"}, {"article_id": "2403.20177", "title": "Artificial consciousness. Some logical and conceptual preliminaries", "authors":"K. Evers, M. Farisco, R. Chatila, B. D. Earp, I. T. Freire, F. Hamker, E. Nemeth, P. F. M. J. Verschure, M.
    Khamassi", "abstract_url":"https://arxiv.org/abs/2403.20177"}, {"article_id": "2403.20151", "title": "A Learning-based Incentive Mechanism for Mobile AIGC Service in
    Decentralized Internet of Vehicles", "authors": "Jiani Fan, Minrui Xu, Ziyao Liu, Huanyi Ye, Chaojie Gu, Dusit Niyato, Kwok-Yan
    Lam", "abstract_url":"https://arxiv.org/abs/2403.20151"}, {"article_id": "2403.20137", "title": "Accurate Block Quantization in LLMs with Outliers", "authors":"Nikita
    Trukhanov, Ilya Soloveychik", "abstract_url":"https://arxiv.org/abs/2403.20137"},{"article_id": "2403.20127", "title": "The Impact of Prompts on Zero-Shot Detection of AI- Generated
    Text", "authors": "Kaito Taguchi, Yujie Gu, Kouichi Sakurai", "abstract_url":"https://arxiv.org/abs/2403.20127"), ("article_id": "2403.20097","title":"ITCMA: A Structure", "authors": "Hanzhong Zhang, Jibin Yin, Haoyang Wang, Ziwei "Implications of the AI Act for Non-Discrimination Law and Algorithmic
    Generative Agent Based on a Computational Consciousness Xiang", "abstract_url":"https://arxiv.org/abs/2403.20097"), ("article_id": "2403.20089", "title":
    Fairness", "authors":"Luca Deck, Jan-Laurin Müller, Conradin Braun, Domenique Zipperling, Niklas Kühl", "abstract_url":"https://arxiv.org/abs/2403.20089"), ("article_id": "2403.19995", "title": "Development of Compositionality and Generalization through Interactive Learning of Language and Action of Robots", "authors": "Prasanna
    Jeffrey Frederic Queisser, Sergio Verduzco Flores, Jun Tani", "abstract_url":"https://arxiv.org/abs/2403.19995"}, ayarch 2403.19992", "title": "MindArm: Mechanized Intelligent Non-Invasive Neuro-Driven Prosthetic Arm System", "authors": "Maha Nawaz, Abdul Basit, Muhammad title": "Diverse Feature Learning by Self-distillation and Reset", "authors":"Sejik
    Vijayaraghavan, Jeff Shafique", "abstract_url":"https://arxiv.org/abs/2483.19992"), ("article_id": "2403.19941", " Wang, Zheng Cui, Boyue Wang, Shirui Pan, Junbin Gao, Baocai Yin, Over Spatiotemporal
    Park", abstract_url":"https://arxiv.org/abs/2403.19941"}, {"article_id": "2403.19883", "title": "Policy-Space Search: Equivalences, Improvements, and " Compression", "authors": "Frederico Messa, André Grahl Pereira", "abstract_url":"https://arxiv.org/abs/2403.19883"), ("article_id": "2403.19881", "title": "IME: Integrating
    Multi-curvature Shared and Specific Embedding for Temporal Knowledge Graph Completion", "authors":"Jiapu Wen Gao", "abstract_url":"https://arxiv.org/abs/2403.19881"), ("article_id": "2403.19857","title":"LLMSense: Harnessing LLMs for High-level Reasoning Mani Srivastava", "abstract_url":"https://arxiv.org/abs/2403.19857"},{"article_id": "2403.19856", "title": "Towards a Brazilian abstract_url":"https://arxiv.org/abs/2403.19856"),
    Sensor Traces", "authors":"Xiaomin Ouyang, History Knowledge Graph", "authors": "Valeria de Paiva, Alexandre Rademaker", " {"article_id": "2403.19826", "title": "Segmentation "}, {"article_id": "2403.19790", "title": "Bespoke Large Language Models for Digital Triage
    Re-thinking Uncertainty Estimation Metrics for Semantic Segmentation", " Masone, Tatiana Tommasi", "abstract_url":"https://arxiv.org/abs/2403.19826 authors":"Qitian Ma, Shyam Nanda Rai, Carlo
    Health Care", "authors": "Niall Taylor, Andrey Kormilitzin, Isabelle Lorge, Alejo Nevado-Holgado, Dan W Yang, Jingyang Zhang, Yifei Ming, Qing Yu, Go Irie, Yixuan Resolution As Language
    Assistance in Mental Joyce", "abstract_url":"https://arxiv.org/abs/2403.19790 "), ("article_id": "2403.19760", "title": "Leveraging Counterfactual Paths for Zakariya Laouar, Zachary Sunberg", " abstract_url":"https://arxiv.org/abs/2403.19760"}, {"article_id": "2403.28331", "title": "Unsolvable
    Contrastive Explanations of POMDP Li, Hai Li, Ziwei Liu, Kiyoharu Aizawa", " of Vision Language Models", "authors": "Atsuyuki Miyai, Jingkang
    Policies", "authors":"Benjamin Kraske, Problem Detection: Evaluating Trustworthiness abstract_url":"https://arxiv.org/abs/2483.20331"}, {"article_id": "2483.20329", "title": "REALM: Reference Saraf, Halim Cagri Ates, Yuan Zhang, Hong Yu, Nidhi Distilled from Large Language
    Modeling", "authors":"Joel Ruben Antony Moniz, Soundarya Krishnan, Melis Ozyildirim, Prathamesh Rajshree", "abstract_url":"https://arxiv.org/abs/2483.20329"},{"article_id": "2483.20327","title":"Gecko: Versatile Text Embeddings Models","authors":"Jinhyuk Lee, Zhuyun Dai, Xiaoqi Ren, Blair Chen, Daniel Cer, Jeremy R. Cole, Kai Hui, Michael Boratko, Rajvi
    Kapadia, Wen Ding, Yi Luan, Sai Meher Jain, Siddhartha Reddy Jonnalagadda, Ming-Wei Chang, Iftekhar Learning", "authors": "Ahmed Agiza, Marina Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects", "authors": "Abhinav Kumar, Yuliang Guo,
    Karthik Duddu, Gustavo Hernandez Abrego, Weiqiang Shi, Nithi Gupta, Aditya Kusupati, Prateek Naim", "abstract_url":"https://arxiv.org/abs/2403.28327"), ("article_id": "2403.28328", "title": "MTLORA: A Low-Rank Adaptation Appro240320318tle":"SeaBird Neseem, Sherief Reda", "abstract_url":"https://arxiv.org/abs/2403.20320"}, {"article_id": "2403.20318","title":"SeaBird: Xinyu Huang, Liu Ren, Xiaoming

![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/5159f2ce-d6f2-4248-a32d-dc9507f7bc84)

## /articles

This endpoint returns a list of articles with information such as the article number, title, publication date, etc. The articles are retrieved using web scraping with BeautifulSoup.

To get a list of all articles with their titles and authors, send a GET request to http://localhost:8000/articles. This will return a JSON object containing a list of articles with their titles and authors.

Request:

    GET request to http://localhost:8000/articles

Response:

![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/3d93c65e-850d-412f-ba07-b20b15a5e440)


## /article/<number>

This endpoint returns the content of a specified article. The content is retrieved using web scraping with BeautifulSoup.

To get information about a specific article, send a GET request to http://localhost:8000/article/{arxiv_id}, where {arxiv_id} is the ID of the article you want to retrieve. This will return a JSON object containing the title, authors, and summary of the article.

Request:

    GET request to http://localhost:8000/article/{arxiv_id}
    
Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/59910f1f-9dbd-47e9-a505-7b735554de47)


## /ml

This endpoint returns the sentiment analysis of all articles using machine learning with TextBlob.

To get the sentiment analysis of all articles, send a GET request to http://localhost:8000/ml. This will return a JSON object containing the sentiment analysis of all articles.

Request:

    GET http://localhost:8000/ml

Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/bffe0c2f-a650-4470-99f9-f67bd0907b89)


## /ml/{number}

This endpoint returns the sentiment analysis of a specific article using machine learning with TextBlob.

To get the sentiment analysis of a specific article, send a GET request to <http://localhost:8000/ml/<number>>, where <number> is the ID of the article. This will return a JSON object containing the sentiment analysis of the article.

Request: 

    GET request to http://localhost:8000/ml/{article_number}

Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/4462c213-6f07-484a-a1f0-f074d4cf9c7e)


## /get_categories

This endpoint returns a list of categories available on arXiv.

To get a list of categories available on arXiv, send a GET request to http://localhost:8000/get_categories. This will return a JSON object containing a list of categories.

Request:

    GET request to http://localhost:8000/get_categories

Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/42db15b1-a14c-48bf-bad9-dcdbcd69e9a6)


## /get_articles/math.CO

This endpoint returns a list of articles in the Combinatorics category with information such as the article number, title, publication date, etc. The articles are retrieved using web scraping with BeautifulSoup.

To get a list of all articles in the Combinatorics category, send a GET request to http://localhost:8000/get_articles/math.CO. This will return a JSON object containing a list of articles with their titles and authors.

Request:

    GET http://localhost:8000/get_articles/math.CO
    
Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/b4a26621-cff6-4faa-a5e1-3a1ea6dec2e9)

## /categories/recent_articles

This endpoint returns a list of recent articles in all categories available on arXiv. The articles are retrieved using web scraping with BeautifulSoup.

To get a list of recent articles in all categories, send a GET request to http://localhost:8000/categories/recent_articles. This will return a JSON object containing a list of recent articles in all categories.

Request:

    GET http://localhost:8000/categories/recent_articles

Response:
![image](https://github.com/Johnny2ki/esilv_api_project/assets/122288399/f2366280-dc10-4fb0-b36b-0a3acea3047d)


## Group Members

The members of the group are listed in the composition.txt file.


## Conclusion

In conclusion, our Project provides an API that fetches news related to Artificial Intelligence from the Arxiv website. We have designed several endpoints to serve different purposes, including fetching a list of articles, displaying article information, accessing the content of a specific article, and executing machine learning scripts for sentiment analysis. Our project uses FastAPI to create the API and BeautifulSoup for web scraping, as well as the TextBlob library for sentiment analysis.

