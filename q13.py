import json
from collections import Counter
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


URL = "https://jsonplaceholder.typicode.com/users"


def top_cities():
    try:
        with urlopen(URL) as response:
            users = json.load(response)

    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")

    except URLError as e:
        print(f"Network Error: {e.reason}")

    else:
        city_counts = Counter(
            user["address"]["city"]
            for user in users
        )

        print("Top 3 Cities with the Most Users:\n")

        for city, count in city_counts.most_common(3):
            print(f"{city}: {count}")


if __name__ == "__main__":
    top_cities()