import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from newspaper import Article
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


# Download required NLTK resources
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
# Download stopwords
nltk.download('stopwords')

def fetch_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def sentiment_analysis(text):
    return TextBlob(text).sentiment

def extract_entities(text):
    tokens = word_tokenize(text)
    tags = pos_tag(tokens)
    tree = ne_chunk(tags)
    
    entities = []
    for subtree in tree:
        if isinstance(subtree, Tree):
            entity = " ".join([word for word, tag in subtree.leaves()])
            entity_type = subtree.label()
            entities.append((entity, entity_type))
    
    return entities

def extract_keywords(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    
    freq_dist = FreqDist(filtered_tokens)
    return [word for word, freq in freq_dist.most_common(10)]

def perform_topic_modeling(texts):
    tokens = [word_tokenize(text.lower()) for text in texts]
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [[token for token in token_list if token.isalnum() and token not in stop_words] for token_list in tokens]
    
    dictionary = corpora.Dictionary(filtered_tokens)
    corpus = [dictionary.doc2bow(token_list) for token_list in filtered_tokens]
    
    lda_model = gensim.models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

    return lda_model.print_topics(num_words=5)

def extract_themes(text):
    entities = extract_entities(text)
    keywords = extract_keywords(text)
    topics = perform_topic_modeling([text])

    return topics

def relevant_info(url):
    content = fetch_article_content(url)
    sentiments = sentiment_analysis(content)
    themes = extract_themes(content)
    return sentiments, content, themes
    