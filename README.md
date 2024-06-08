# BuildClub AI Hackathon - Music for Reading

> Idea: Music recommendation based on Article reading at that point in time

## Background

As a University student studying in my third year, I have come across many articles throughout my life which I have read with my music most of the time. As an avid lover of music, I tend to focus more when there is something playing in the background as I love multitasking. However, sometimes I found that the music that I play through `Spotify` may not apt for a news article or a research paper I am reading, for example. Imagine playing an upbeat pop song over an article that mourns the death of a lover!

To address this issue, I decided that I wanted to tackle this problem as a part of this hackathon. I wanted to solve this issue by trying to code a simple chatbot that recommends you music when in you drop an article that you want to read, which complies with the theme "better for the world" is because it makes focus a lot better and you also get recommended music on the same. Take that, Spotify! (I'm jk :P)

## Functionality

The directory structure is as follows:

``` (Drawing)
code (folder):
    > data (folder):
        > tcc_ceds_music.csv -> contains the music dataset
    > app.py -> main file to run
    > article_analysis.py -> analyses the content in the url given
    > music_analysis.py -> analyses the music from the kaggle dataset
    > recommender.py -> recommends the music
```

The way we can use this is also as follows:

1. Using `Julep.AI`, I implemented a simple chatbot that simply asks the user to input any article that they would like me to recommend their music for.
2. Then, using `pandas`, `nltk` and `TextBlob`, I perform a sentiment analysis on the content that the article provides me. As a tip, I also take the regex etc into account because if it consists of emojis then I would like it to be counted towards the sentiment analysis (to determine polarity).
3. Then, using `scikit TfidfVectorizer`, I convert the content into a tf-idf vector so I can begin my search through similarity scores and sentiment analysis, comparing the scores for both the music and the article and gauging which similarity score ends up benefitting us.
4. After the search, I end up returning a list of music that could be listened to while reading said article.

## Future

In the future, I would like to develop this into an extension so that people do not need to input an article into the chatbot and can instead access the website directly.

I would also like to implement semantic routing to filter any explicit content mentioned within the article and anything that is specifically racist/politically influential.
