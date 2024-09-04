#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    return number of subscribers of a subreddit
    """

    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={'User-Agent': 'Omar Talat'},
        allow_redirects=False
    )
    if response.status_code == 404:
        return 0
    dict_ = response.json()
    return dict_.get('data').get('subscribers')
