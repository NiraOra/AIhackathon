import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# analysing the music data over here so we can compare
# Fetch and preprocess music data
# Example data Used: taken from https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019
response_music = pd.read_csv('data/tcc_ceds_music.csv')
music_sentiment = [ 
    TextBlob(lyric).sentiment for lyric in response_music['lyrics']
]

def extract_features_from_lyrics(lyrics):
    # Tokenize and remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(lyrics.lower())
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    
    # Frequency Distribution
    freq_dist = FreqDist(filtered_tokens)
    
    sentiment_scores = TextBlob(lyrics).sentiment
    
    return filtered_tokens, freq_dist, sentiment_scores

def data():
    return music_sentiment

# match the index to the track name
def get_track(index):
    return response_music['track_name'][index]