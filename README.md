# AI hackthon Project, specs and etc

Idea: Music recommendation based on Article reading at that point in time

## Background

As a _____. I wanted to solve this issue by trying to code a simple chatbot that recommends you music when in you drop an article that you want to read.

The reason why this complies with the theme "better for the world" is because it makes focus a lot better and you also get recommended music on the same.

## Functionality

The directory structure is as follows:

The way we can use this is also as follows:

1. Using `Julep.AI`, I implemented a simple chatbot that simply asks the user to input any article that they would like me to recommend their music for.
2. Then, using `pandas` and `TextBlob`, I perform a sentiment analysis on the content that the article provides me. As a tip, I also take the regex etc into account because if it consists of emojis then I would like it to be counted towards the sentiment analysis (to determine polarity).
3. Then, using `scikit`, I convert the content into a tf-idf vector so I can begin my search through cosine similarity and etc.
4. After the search, I end up returning a list of music that could be listened to while reading said article.

Demo: __

## Future:

In the future, I would like to develop this into an extension so that people do not need to input an article into the chatbot and can instead access the website directly. I was not able to do this on time, so I would like to put it out here.