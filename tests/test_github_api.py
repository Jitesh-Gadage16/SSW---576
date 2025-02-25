import requests

def test_github_api():
    response = requests.get("https://api.github.com/users/octocat/repos")
    assert response.status_code == 200
