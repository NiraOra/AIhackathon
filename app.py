import pandas as pd
# import julep
from textblob import TextBlob
# from julep import AsyncClient
# -> later used for data extraction from websites
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import article_analysis
import music_analysis
import recommender

# TODO: csv file example from where music is from
response_music = pd.read_csv('data/tcc_ceds_music.csv')

# # TODO: using Julep AI
# JULEP_API_KEY = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NTcyM2I5Yy04MTgxLTQwOTMtODhhMC1hMjE2NzdhYWFjNzYiLCJlbWFpbCI6Im5pcmFhcnVubWVub25AZ21haWwuY29tIiwiaWF0IjoxNzE3ODIwMzIyLCJleHBpcmVzSW4iOiIxeSIsInJhdGVMaW1pdFBlck1pbnV0ZSI6MzUwMCwicXVvdGFSZXNldCI6IjFoIiwiY2xpZW50RW52aXJvbm1lbnQiOiJzZXJ2ZXIiLCJzZXJ2ZXJFbnZpcm9ubWVudCI6InByb2R1Y3Rpb24iLCJ2ZXJzaW9uIjoidjAuMiIsImV4cCI6MTc0OTM3NzkyMn0._JIGxAoEiZ7VpypUcGLbClSVumwK_mumRBJ_eitfwaCQzY-V9_bkIkh_HkjRd7KV6SHNiIWQRjckWGCa5OWtIA"
# JULEP_BASE_URL = "https://dev.julep.ai/api"

# client = AsyncClient(api_key=JULEP_API_KEY, base_url=JULEP_BASE_URL)

# to take care: OFFENSIVE MUSIC TO NOT BE ALLOWED
# includes: racist songs, NSFW or explicit

# # Analysing the article first
# example = article_analysis.relevant_info("https://www.opencolleges.edu.au/blogs/articles/our-best-ever-study-playlist")
example = "https://www.opencolleges.edu.au/blogs/articles/our-best-ever-study-playlist"
# # get the music so we can analyse that too
# music = music_analysis.data()
# example: 
recommender.recommend_music(example)

print(example)


