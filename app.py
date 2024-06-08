import pandas as pd
# import julep
from textblob import TextBlob
# from julep import AsyncClient
# -> later used for data extraction from websites
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from newspaper import Article

# Getting the article Content using the URL
def fetch_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def sentiment_analysis(text):
    return TextBlob(text).sentiment

# # using Julep AI
# JULEP_API_KEY = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NTcyM2I5Yy04MTgxLTQwOTMtODhhMC1hMjE2NzdhYWFjNzYiLCJlbWFpbCI6Im5pcmFhcnVubWVub25AZ21haWwuY29tIiwiaWF0IjoxNzE3ODIwMzIyLCJleHBpcmVzSW4iOiIxeSIsInJhdGVMaW1pdFBlck1pbnV0ZSI6MzUwMCwicXVvdGFSZXNldCI6IjFoIiwiY2xpZW50RW52aXJvbm1lbnQiOiJzZXJ2ZXIiLCJzZXJ2ZXJFbnZpcm9ubWVudCI6InByb2R1Y3Rpb24iLCJ2ZXJzaW9uIjoidjAuMiIsImV4cCI6MTc0OTM3NzkyMn0._JIGxAoEiZ7VpypUcGLbClSVumwK_mumRBJ_eitfwaCQzY-V9_bkIkh_HkjRd7KV6SHNiIWQRjckWGCa5OWtIA"
# JULEP_BASE_URL = "https://dev.julep.ai/api"

# client = AsyncClient(api_key=JULEP_API_KEY, base_url=JULEP_BASE_URL)

# sample dataset from kaggle for now

# # Fetch and preprocess article data
response_articles = pd.read_csv('data/Articles.csv') # taken from https://www.kaggle.com/datasets/dorianlazar/medium-articles-dataset
articles = pd.DataFrame(response_articles)

# # Fetch and preprocess music data
response_music = pd.read_csv('data/tcc_ceds_music.csv') # taken from https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019
music_tracks = pd.DataFrame(response_music)

# article_content = articles['Article']
article_sentiment = [
    TextBlob(article).sentiment for article in articles['Article']
]

music_content = response_music['lyrics']
music_sentiment = [
    TextBlob(lyric).sentiment for lyric in response_music['lyrics']
]


# to extract content from website
# for url in urls:
#     print(requests.get(urls).text)

# # Combine article and music data into one corpus
combined_data = pd.concat([articles['Article'], music_tracks['track_name']], ignore_index=True)

# # Prepare the TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(combined_data)

# Compute cosine similarity for the combined data
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get music recommendations based on an article
def get_music_recommendations(article_title, cosine_sim=cosine_sim):
    article_idx = articles[articles['Article'] == article_title].index[0]
    # music data starts after articles in combined data
    music_start_idx = len(articles)  
    sim_scores = list(enumerate(cosine_sim[article_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [score for score in sim_scores if score[0] >= music_start_idx][:10]
    music_indices = [i[0] - music_start_idx for i in sim_scores]
    return music_tracks['track_name'].iloc[music_indices]

# to take care: OFFENSIVE MUSIC TO NOT BE ALLOWED
# includes: racist songs, NSFW or explicit

# recommendations = get_music_recommendations(articles['Article'][2])
# print(f"For title: {articles['Article'][2]}, we ended up getting the following recommendations: {recommendations}")
example = fetch_article_content("https://www.opencolleges.edu.au/blogs/articles/our-best-ever-study-playlist")
print(sentiment_analysis(example))

