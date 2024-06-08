from textblob import TextBlob
from newspaper import Article

# use the url and get the content
def fetch_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# analyses the article based on url atm and then returns the sentiment score, content and themes
def relevant_info(url):
    content = fetch_article_content(url)
    sentiments = TextBlob(content).sentiment
    return sentiments, content
