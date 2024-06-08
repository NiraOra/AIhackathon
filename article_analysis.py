import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import gensim
from gensim import corpora
from textblob import TextBlob
from newspaper import Article
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Download required NLTK resources (download only once at the beginning)
nltk.download('punkt', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('stopwords', quiet=True)


def fetch_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# processes the text to make it easier for extraction
def preprocess_text(text):
  tokens = word_tokenize(text.lower())
  stop_words = set(stopwords.words('english'))
  return [token for token in tokens if token.isalnum() and token not in stop_words]

# extracts the entities of the text (based on Proper words, dates, etc)
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

# takes the keywords of the content
def extract_keywords(text):
    preprocessed_text = preprocess_text(text)
    freq_dist = FreqDist(preprocessed_text)
    return [word for word, freq in freq_dist.most_common(10)]


# Performs topic modeling on the content using LDA.
def perform_topic_modeling(text):
    preprocessed_text = [preprocess_text(text)]
    dictionary = corpora.Dictionary(preprocessed_text)
    corpus = [dictionary.doc2bow(doc) for doc in preprocessed_text]
    
    lda_model = gensim.models.LdaModel(corpus, num_topics=1, id2word=dictionary, passes=15)
    return lda_model.print_topics(num_words=5)[0]

# analyses the article based on url atm and then returns the sentiment score, content and themes
def relevant_info(url):
    content = fetch_article_content(url)
    sentiments = TextBlob(content).sentiment
    themes = perform_topic_modeling(content)
    return sentiments, content, themes
