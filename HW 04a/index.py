import requests
import json

def get_github_repos(user_id):
    """
    Retrieves all repositories for a given GitHub user and fetches the number of commits for each repository.
    """
    base_url = f"https://api.github.com/users/{user_id}/repos"
    try:
        response = requests.get(base_url)
        if response.status_code != 200:
            return f"Error: Unable to fetch repositories. Status Code {response.status_code}"

        repos = response.json()
        repo_commit_counts = []

        for repo in repos:
            repo_name = repo["name"]
            commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
            commit_response = requests.get(commits_url)

            if commit_response.status_code == 200:
                commit_count = len(commit_response.json())
            else:
                commit_count = "Error fetching commits"

            repo_commit_counts.append(f"Repo: {repo_name} Number of commits: {commit_count}")

        return repo_commit_counts

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Example usage:
if __name__ == "__main__":
    user_id = input("Enter GitHub Username: ")
    results = get_github_repos(user_id)
    for result in results:
        print(result)
