# LangChain Spotify Assistant

A simple Python script that uses the LangChain library to create a Spotify chatbot agent. It relies on the OpenAI API and Spotipy library to interact with Spotify in a conversational manner.

## Dependencies

- [LangChain](https://langchain.io)
- [OpenAI API](https://www.openai.com/api/)
- [Spotipy](https://spotipy.readthedocs.io/)
- [Requests](https://docs.python-requests.org/)
- [PyYAML](https://pyyaml.org/)

## Setup

1. Install required libraries:

   ```
   pip install langchain openai spotipy requests pyyaml
   ```

2. Set the following environment variables:

   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `SPOTIPY_CLIENT_ID`: Your Spotify client ID.
   - `SPOTIPY_CLIENT_SECRET`: Your Spotify client secret.
   - `SPOTIPY_REDIRECT_URI`: Your Spotify app redirect URI.
 
   Alternatively, you can replace the placeholders in the following lines of the code with the corresponding values:

   ```
   os.environ["OPENAI_API_KEY"]="replace"
   os.environ["SPOTIPY_CLIENT_ID"]="replace"
   os.environ["SPOTIPY_CLIENT_SECRET"]="replace"
   os.environ["SPOTIPY_REDIRECT_URI"]="replace"
   ```

## Usage

Run `spotify_assistant.py`:

```
python spotify_assistant.py
```

Then, the script will prompt you to enter your user query. As an example:

```
Tell your Spotify assistant what to do: Play my playlist called "Workout"
```

## How it works

1. Downloads the [Spotify API OpenAPI Specification](https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/spotify.com/1.0.0/openapi.yaml) to create an intelligent agent using the LangChain library.
2. Obtains the scope definitions and requests a token for user authentication.
3. Initializes the `ChatOpenAI` model using GPT-4 and `RequestsWrapper` to handle the authentication while communicating with the Spotify API.
4. Receives user input and sends it to the LangChain-driven Spotify agent.
5. Prints the agent's response to the console.