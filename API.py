import requests
from dataclasses import dataclass


@dataclass
class Repository:
    """
    A class to represent a repository.
    :ivar name: The name of the repository.
    :ivar stars: The amount of stars.
    :ivar language: The program language.
    """
    name: str
    stars: int
    language: str
    
    def __str__(self):
        return f"{self.name} is a {self.language} repo with {self.stars} stars."


def requests_top_repos(language: str, num_of_repos: int) -> list:
    """
    The function requests the popular repositories in GitHub by language.
    :param language:The programing language of the repos
    :param num_of_repos: Count of repos to request
    :return: list of the popular repositories that return from GitHub API
    """
    query = f"https://api.github.com/search/repositories?q=language:{language}&per_page:{num_of_repos}&sort:stars"
    answer_repos = requests.get(query)
    return [Repository(item['name'],item['watchers'],language) for item in answer_repos.json()['items']]


def main():
    [print(repo) for repo in requests_top_repos("python",20)]


if __name__ == "__main__":
    main()
"""
example :

Python is a Python repo with 135151 stars.
awesome-python is a Python repo with 125409 stars.
Python-100-Days is a Python repo with 117693 stars.
django is a Python repo with 63742 stars.
transformers is a Python repo with 61716 stars.
HelloGitHub is a Python repo with 54842 stars.
requests is a Python repo with 47325 stars.
openpilot is a Python repo with 34228 stars.
d2l-zh is a Python repo with 31876 stars.
XX-Net is a Python repo with 31210 stars.
sentry is a Python repo with 30752 stars.
certbot is a Python repo with 28864 stars.
wtfpython is a Python repo with 28612 stars.
HanLP is a Python repo with 25736 stars.
airflow is a Python repo with 25632 stars.
yt-dlp is a Python repo with 24187 stars.
YouCompleteMe is a Python repo with 23916 stars.
django-rest-framework is a Python repo with 23274 stars.
spaCy is a Python repo with 23225 stars.
sqlmap is a Python repo with 23296 stars.
ItChat is a Python repo with 22151 stars.
MockingBird is a Python repo with 21043 stars.
algo is a Python repo with 20768 stars.
algorithms is a Python repo with 20687 stars.
hosts is a Python repo with 20544 stars.
glances is a Python repo with 20351 stars.
NLP-progress is a Python repo with 20217 stars.
ray is a Python repo with 20150 stars.
celery is a Python repo with 19213 stars.
GFPGAN is a Python repo with 19144 stars.
"""
