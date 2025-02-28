import unittest
from unittest.mock import patch, MagicMock
import requests
from index import get_github_repos 

class TestGitHubAPI(unittest.TestCase):

    @patch("requests.get")
    def test_valid_user(self, mock_get):
        """Test a valid user with repositories"""
        mock_repos_response = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_commits_response = [{"commit": "data"}] * 5  

        # Create mock response objects
        mock_repo_response_obj = MagicMock(status_code=200)
        mock_repo_response_obj.json.return_value = mock_repos_response

        mock_commit_response_obj = MagicMock(status_code=200)
        mock_commit_response_obj.json.return_value = mock_commits_response

        # Mock API responses
        mock_get.side_effect = [mock_repo_response_obj, mock_commit_response_obj, mock_commit_response_obj]

        expected_output = [
            "Repo: repo1 Number of commits: 5",
            "Repo: repo2 Number of commits: 5"
        ]
        self.assertEqual(get_github_repos("valid_user"), expected_output)

    @patch("requests.get")
    def test_invalid_user(self, mock_get):
        """Test an invalid user (404 Not Found)"""
        mock_get.return_value = MagicMock(status_code=404, json=lambda: {"message": "Not Found"})
        self.assertEqual(get_github_repos("invalid_user"), "Error: Profile not found or username 'invalid_user' does not exist.")

    @patch("requests.get")
    def test_no_repos(self, mock_get):
        """Test a valid user with no repositories"""
        mock_get.return_value = unittest.mock.Mock(status_code=200, json=lambda: [])
        self.assertEqual(get_github_repos("user_with_no_repos"), "User 'user_with_no_repos' has no public repositories.")

    @patch("requests.get")
    def test_rate_limit_exceeded(self, mock_get):
        """Test GitHub API rate limit exceeded (403 Forbidden)"""
        mock_get.return_value = MagicMock(status_code=403, json=lambda: {"message": "API rate limit exceeded"})
        self.assertEqual(get_github_repos("any_user"), "Error: Unable to fetch repositories. Status Code 403")

    @patch("requests.get")
    def test_network_error(self, mock_get):
        """Test a network error scenario"""
        mock_get.side_effect = requests.exceptions.RequestException("Network failure")
        self.assertEqual(get_github_repos("any_user"), "Request failed: Network failure")

if __name__ == "__main__":
    unittest.main()
