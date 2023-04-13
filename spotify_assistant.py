import os
os.environ["OPENAI_API_KEY"]="replace"
os.environ["SPOTIPY_CLIENT_ID"]="replace"
os.environ["SPOTIPY_CLIENT_SECRET"]="replace"
os.environ["SPOTIPY_REDIRECT_URI"]="replace"

from langchain.llms.openai import OpenAI
from langchain.agents.agent_toolkits.openapi import planner
from langchain.chat_models import ChatOpenAI
import spotipy.util as util
from langchain.requests import RequestsWrapper
from langchain.agents.agent_toolkits.openapi.spec import reduce_openapi_spec

import requests
import yaml

def save_api_spec(api_url, api_file):
    response = requests.get(api_url)
    with open(api_file, 'w') as f:
        f.write(response.text)

save_api_spec('https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/spotify.com/1.0.0/openapi.yaml', 'spotify_openapi.yaml')

with open("spotify_openapi.yaml") as f:
    raw_spotify_api_spec = yaml.load(f, Loader=yaml.Loader)
spotify_api_spec = reduce_openapi_spec(raw_spotify_api_spec)

def construct_spotify_auth_headers(raw_spec: dict):
    scopes = list(raw_spec['components']['securitySchemes']['oauth_2_0']['flows']['authorizationCode']['scopes'].keys())
    access_token = util.prompt_for_user_token(scope=','.join(scopes))
    return {
        'Authorization': f'Bearer {access_token}'
    }

# Get API credentials.
headers = construct_spotify_auth_headers(raw_spotify_api_spec)
requests_wrapper = RequestsWrapper(headers=headers)

llm = ChatOpenAI(model_name="gpt-4", temperature=0.0)
spotify_agent = planner.create_openapi_agent(spotify_api_spec, requests_wrapper, llm)

user_query = input("Tell your Spotify assistant what to do: ")
response = spotify_agent.run(user_query)
print(response)