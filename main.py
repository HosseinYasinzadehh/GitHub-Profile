import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url)
    response.raise_for_status()
    result = response.json()

    print(f"Username: {result['login']}")
    print(f"Name: {result['name']}")
    print(f"Public repositories: {result['public_repos']}")
    print(f"Followers: {result['followers']}")
    print(f"Following: {result['following']}")
    print(f"Profile: {result['html_url']}")

except requests.exceptions.HTTPError as http:
    if response.status_code == 404:
        print("User not found.")
    else:
        print(f"error: {http}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
