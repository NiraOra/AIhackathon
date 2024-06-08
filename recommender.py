# do all the recommender system operations here
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import music_analysis
import pandas as pd
import article_analysis

response_music = pd.read_csv('data/tcc_ceds_music.csv')

def calculate_similarity(article_tokens, music_tokens):
    # Combine tokens to create documents
    article_text = ' '.join(article_tokens)
    music_text = ' '.join(music_tokens)
    
    # Vectorize the text
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([article_text, music_text])

    return cosine_similarity(tfidf_matrix[:1], tfidf_matrix[1:2])[0][0]

# Example usage
def recommend_music(article_url, music_data=response_music):
    recommendations = []
    # extracting features of the article
    (article_polarity, article_sentiment), article_content, article_themes = article_analysis.relevant_info(article_url)
    # for each lyric
    for idx, row in music_data.iterrows():
        lyrics = row['lyrics']
        music_tokens, music_freq_dist, (music_polarity, music_sentiment) = music_analysis.extract_features_from_lyrics(lyrics)
        
        # Calculate similarity score
        similarity_score = calculate_similarity(article_content, music_tokens)
        
        # Compare sentiment scores
        sentiment_difference = abs(article_polarity - music_sentiment)
        
        # Combine scores (e.g., weighted sum)
        combined_score = (similarity_score * 0.7) - (sentiment_difference * 0.3)
        
        recommendations.append((row['artist_name'], row['track_name'], combined_score))
    
    # Sort recommendations by combined score
    recommendations.sort(key=lambda x: x[2], reverse=True)
    
    return recommendations[:5]  # Return top 5 recommendations



