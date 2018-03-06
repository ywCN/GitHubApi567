import requests
import json


def get_repo_info():
    user_url = 'https://api.github.com/users/ywang567/repos'
    res = requests.get(user_url)
    return json.loads(res.text)

def get_commit_info(repo_name):
    repo_url = 'https://api.github.com/repos/ywang567/{}/commits'.format(repo_name)
    repo_info = requests.get(repo_url)
    return json.loads(repo_info.text)

def get_user_info():
    user_info = []
    repos = get_repo_info()
    print('repos are', repos)
    user_info.append('User: ywang567')

    try:
        repos[0]['name']
    except (TypeError, KeyError, IndexError):
        return 'unable to fetch repos from user'

    for repo in repos:
        repo_info_json = get_commit_info(repo['name']);
        # print(repo_info_json)
        user_info.append('Repo: {} Number of commits: {}'.format(repo['name'], len(repo_info_json)))

    return user_info


if __name__ == '__main__':
    for entry in get_repo_info():
        print(entry)
