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
    print("Here are some music recommendations for the article:")
    for (name, song, _) in recommendations:
        print(f"\t{name} - {song}")
    print("Hope you enjoyed these recommendations!")
    
# Analysing the article first
example = "https://www.opencolleges.edu.au/blogs/articles/our-best-ever-study-playlist"
example_sad = "https://au.finance.yahoo.com/news/sad-reality-aussie-workforce-043318613.html"
example_ok = "https://7news.com.au/sport/afl/afl-coach-simon-goodwin-makes-sad-admission-about-relentless-media-attack-c-14953976"
# getting the music that was recommended based on the url
music = recommender.recommend_music(example)
# printing out the results
pretty_print(music)

#TODO: JULEPAI
# to make sure it is a valid url
# def get_user_input():
#   """Prompts the user for an article URL and returns it."""
#   while True:
#     url = input("Enter an article URL (or 'q' to quit): ")
#     if url.lower() == 'q':
#       return None
#     if not url.startswith("http"):
#       print("Invalid URL. Please enter a valid http or https URL.")
#       continue  # Loop back to prompt for a valid URL
#     return url



# recommendation
# def rec(url: str):
#     return recommender.recommend_music(url)

# while True:
#     # Initiate conversation with Julep using pre-defined prompts
#     print(INSTRUCTIONS[0])

#     messages = [
#         {
#             "role": "system",
#             "content": 'Hello! How may I help you today?'
#         },
#         {
#             "role": "user",
#             "input": "user"
#         }
#     ]

#     chat_completion = client.chat.completions.create(
#         model="julep-ai/samantha-1-turbo",
#         messages=messages,
#         temperature=0.7,
#         max_tokens=200,
#         top_p=1
#     )

#     # Get user input for the URL
#     url = get_user_input()
#     if not url:
#         break  # User entered 'q' to quit

#     if recommendations := rec(url):
#         pretty_print(recommendations)
#     else:
#         print("Sorry, I couldn't find any music recommendations for that article.")

# print("Thanks for using DeVsMond! See you next time.")

# messages = [
#     {
#         "role": "instruction",
#         "name": "DeVsMond",
#         "situation": SITUATION_PROMPT
#     },
#     {
#         "role": "user",
#         "input": "user"
#     }
# ]

# chat_completion = client.chat.completions.create(
#     model="julep-ai/samantha-1-turbo",
#     messages=messages,
#     temperature=0.7,
#     max_tokens=200,
#     top_p=1
# )

# while True:
#     url = input("Enter an article URL (or 'q' to quit): ")

#     # Check for quit command
#     if url.lower() == 'q':
#         break

#     # Use the URL to get recommendations
#     try:
#         result = recommender.recommend_music(url)
#         print(f"Music recommendations for the article: {result}")
#     except Exception as e:
#         print(f"Error retrieving recommendations: {e}")

# print(chat_completion.choices[0].message.content)


# # # description stuff 
# def rec(url: str):
#     result = recommender.recommend_music(url)
#     return result

# TOOLS = [
#     {
#         "type": "function",
#         "function": {
#             "name": "rec",
#             "description": "Takes the url and returns a list of 5 music items.",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "url": {
#                         "type": "string",
#                         "description": "The url to be used to recommend the music.",
#                     }
#                 },
#                 "required": ["url"],
#             },
#         },
#     },
# ]

# # AGENT
# agent = client.agents.create(
#     name="DeVsMond",
#     about="An agent that provides music recommendations based on the article given",
#     tools=TOOLS,
#     instructions=INSTRUCTIONS,
#     model="gpt-3.5",
#     default_settings={
#         "temperature": 0.5,
#         "top_p": 1,
#         "min_p": 0.01,
#         "presence_penalty": 0,
#         "frequency_penalty": 0,
#         "length_penalty": 1.0,
#     },
#     metadata={"name": "DeVsMond"},
# )

# # USER
# user = client.users.create(
#     name="Anon",
#     about="A user that inputs the article url, expecting an output of music",
#     metadata={"name": "Anon"},
# )


# # Now, making a session
# session = client.sessions.create(
#     user_id=user.id,
#     agent_id=agent.id,
#     situation=SITUATION_PROMPT,
#     metadata={"agent_id": agent.id, "user_id": user.id},
# )




