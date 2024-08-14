#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/91.0.4472.124 Safari/537.36'
        ),
        'Accept': 'application/json',
        'Connection': 'keep-alive'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from Reddit API: {e}")
        return 0

    try:
        # Attempt to parse the JSON response
        data = response.json().get("data")
        if data is None:
            return 0
        return data.get("subscribers", 0)
    except ValueError:
        # Handle the case where the response is not JSON
        print("Error: Received an invalid JSON response")
        return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
    else:
        print("Please provide a subreddit name.")
