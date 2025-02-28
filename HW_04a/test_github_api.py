import unittest
from unittest.mock import patch
import requests

class TestGitHubAPI(unittest.TestCase):

    @patch("requests.get")
    def test_valid_user_with_repos(self, mock_get):
        """Test a valid user with repositories"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]

        response = requests.get("https://api.github.com/users/octocat/repos")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 2)
        self.assertIn("name", response.json()[0])  # Ensure each repo has a "name"

    @patch("requests.get")
    def test_user_not_found(self, mock_get):
        """Test a non-existent user (404 Not Found)"""
        mock_get.return_value.status_code = 404

        response = requests.get("https://api.github.com/users/nonexistentuser/repos")
        self.assertEqual(response.status_code, 404)

    @patch("requests.get")
    def test_user_has_no_repositories(self, mock_get):
        """Test a valid user with no repositories"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []

        response = requests.get("https://api.github.com/users/user_without_repos/repos")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)  # Ensure empty repo list

    @patch("requests.get")
    def test_api_rate_limit_exceeded(self, mock_get):
        """Test GitHub API rate limit exceeded (403 Forbidden)"""
        mock_get.return_value.status_code = 403

        response = requests.get("https://api.github.com/users/octocat/repos")
        self.assertEqual(response.status_code, 403)

    @patch("requests.get")
    def test_network_error(self, mock_get):
        """Test network-related errors (Connection timeout, DNS failure, etc.)"""
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        with self.assertRaises(requests.exceptions.RequestException):
            requests.get("https://api.github.com/users/octocat/repos")

if __name__ == "__main__":
    unittest.main()
