import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# URLs for the backend and sentiment analyzer service
backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

# Function to perform a GET request
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"
    
    request_url = backend_url + endpoint + "?" + params
    print(f"GET from {request_url}")
    
    try:
        response = requests.get(request_url)
        return response.json()
    except:
        print("Network exception occurred")

# Function to analyze the sentiment of a review text
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

# Function to post a review to the backend
def post_review(data_dict):
    request_url = backend_url + "/insert_review"  # Assuming backend URL and endpoint
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())  # Log the response for debugging
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
