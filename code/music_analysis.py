from textblob import TextBlob

# just extracts features from the music
def extract_features_from_lyrics(lyrics):
    return TextBlob(lyrics).sentiment