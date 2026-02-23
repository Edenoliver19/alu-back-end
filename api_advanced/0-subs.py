#!/usr/bin/python3
"""
Return the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers, 0 if invalid subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "linux:alu-scripting:student:v1.0 (by /u/anonymous)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            return 0

        results = response.json()
        return results.get("data").get("subscribers")

    except Exception:
        return 0
