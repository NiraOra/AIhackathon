import pandas as pd
import requests 
# -> later used for data extraction from websites
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify

# sample dataset from kaggle for now

# Fetch and preprocess article data
response_articles = pd.read_csv('data/Articles.csv') # taken from https://www.kaggle.com/datasets/dorianlazar/medium-articles-dataset
articles = pd.DataFrame(response_articles)

# Fetch and preprocess music data
response_music = pd.read_csv('data/tcc_ceds_music.csv') # taken from https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019
music_tracks = pd.DataFrame(response_music)

# # to extract content from website
# for url in urls:
#     print(requests.get(urls).text)

# Combine article and music data into one corpus
combined_data = pd.concat([articles['Article'], music_tracks['genre']], ignore_index=True)

# Prepare the TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(combined_data)

# # Compute cosine similarity for the combined data
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# # Function to get music recommendations based on an article
def get_music_recommendations(article_title, cosine_sim=cosine_sim):
    article_idx = articles[articles['Article'] == article_title].index[0]
    music_start_idx = len(articles)  # music data starts after articles in combined data
    sim_scores = list(enumerate(cosine_sim[article_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [score for score in sim_scores if score[0] >= music_start_idx][:10]
    music_indices = [i[0] - music_start_idx for i in sim_scores]
    return music_tracks['title'].iloc[music_indices]

# app = Flask(__name__)

# @app.route('/recommend', methods=['GET'])
# def recommend():
#     title = request.args.get('title')
#     recommendations = get_music_recommendations(title)
#     return jsonify(recommendations.tolist())

# if __name__ == '__main__':
#     app.run(debug=True)
