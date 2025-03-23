import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {}".format(request_url))

    try:
        response = requests.get(request_url)
        print(response)
        return response.json()
    except Exception:
        print("Network exception occurred")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text

    try:
        response = requests.get(request_url)
        
        # Check if the response is successful and contains the expected data
        if response.status_code == 200:
            sentiment_data = response.json()
            if sentiment_data and 'sentiment' in sentiment_data:
                return sentiment_data
            else:
                print(f"Sentiment data missing in response: {sentiment_data}")
                return {"sentiment": "unknown"}  # Return a default value if sentiment is not found
        else:
            print(f"Error: Received {response.status_code} from sentiment analyzer")
            return {"sentiment": "unknown"}  # Return default value in case of non-200 response

    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"sentiment": "unknown"}  # Return a default value if the request fails



def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception:
        print("Network exception occurred")
