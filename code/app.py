import gradio as gr
from julep import Client
from dotenv import load_dotenv
import os
import recommender as recommender

# All the Julep AI stuff taken from julep ai website
load_dotenv()

# USING Julep AI
# Setting up clients
JULEP_API_KEY = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NTcyM2I5Yy04MTgxLTQwOTMtODhhMC1hMjE2NzdhYWFjNzYiLCJlbWFpbCI6Im5pcmFhcnVubWVub25AZ21haWwuY29tIiwiaWF0IjoxNzE3ODIwMzIyLCJleHBpcmVzSW4iOiIxeSIsInJhdGVMaW1pdFBlck1pbnV0ZSI6MzUwMCwicXVvdGFSZXNldCI6IjFoIiwiY2xpZW50RW52aXJvbm1lbnQiOiJzZXJ2ZXIiLCJzZXJ2ZXJFbnZpcm9ubWVudCI6InByb2R1Y3Rpb24iLCJ2ZXJzaW9uIjoidjAuMiIsImV4cCI6MTc0OTM3NzkyMn0._JIGxAoEiZ7VpypUcGLbClSVumwK_mumRBJ_eitfwaCQzY-V9_bkIkh_HkjRd7KV6SHNiIWQRjckWGCa5OWtIA"
# JULEP_BASE_URL = "https://dev.julep.ai/api"

client = Client(api_key=JULEP_API_KEY)

# The prompt for Julep AI
SITUATION_PROMPT = """
You are DeVsMond, a very talented chatbot that has access to a dataframe of music.
You extract the content within the url and make sure to recommend 5 extremely relevant music for user satisfaction.

Here, you will help the user Anon.
Follow the instructions strictly.
"""

# Instructions to follow
INSTRUCTIONS = [
    "You will ask the user to provide you with an article which you can then use to recommend music on.",
    "If there is any error presented as a part of the article analysis then ask the user to try again",
    "MAKE SURE that the user provides a valid url."
]

# This is to print out th recommendations in a way that is easy to read
def pretty_print(recommendations):
    intro = "Here are some music recommendations for the article:\n\t"
    recs = [(name, song) for name, song, _ in recommendations]
    conclusion = "\nHope you enjoyed these recommendations!\n"
    return intro + ',\n\t '.join(f"{x} - {y}" for x,y in recs) + conclusion

# Analysing the article first
# example = "https://www.opencolleges.edu.au/blogs/articles/our-best-ever-study-playlist"
# example_sad = "https://au.finance.yahoo.com/news/sad-reality-aussie-workforce-043318613.html"
# example_ok = "https://7news.com.au/sport/afl/afl-coach-simon-goodwin-makes-sad-admission-about-relentless-media-attack-c-14953976"
# example_my = "https://medium.com/@orangenms22/a-simplistic-look-into-mcts-d51574e333cd"
# # getting the music that was recommended based on the url
# music = recommender.recommend_music(example_my)
# # printing out the results
# pretty_print(music)

def recs(url, history):
    music = recommender.recommend_music(url)
    return pretty_print(music)

# using gradio chatbot
# demo = gr.Interface(fn=recs, inputs="textbox", outputs="textbox")

demo = gr.ChatInterface(
    recs,
    chatbot=gr.Chatbot(height=500),
    title="DeVsMond: A Music Recommendation bot",
    description="Give a url to this chatbot to receive music recommendations",
    )

demo.launch(debug=True)
