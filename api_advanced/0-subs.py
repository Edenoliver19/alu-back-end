#!/usr/bin/python3
"""
Return the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers, 0 if invalid"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "linux:alu-project:v1.0 (by /u/anonymous)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )


        if response.status_code != 200:
            return 0

        return response.json().get("data", {}).get("subscribers", 0)

    except Exception:
        return 0
