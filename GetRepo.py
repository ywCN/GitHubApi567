import requests
import json


def get_repo_info():
    user_url = 'https://api.github.com/users/ywang567/repos'
    res = requests.get(user_url)
    return json.loads(res.text)

def get_commit_info(repos):
    commit_info = []
    for repo in repos:
        repo_name = repo['name']
        repo_url = 'https://api.github.com/repos/ywang567/{}/commits'.format(repo_name)
        repo_info = requests.get(repo_url)
        repo_info_json = json.loads(repo_info.text)
        commit_info.append('Repo: {} Number of commits: {}'.format(repo_name, len(repo_info_json)))

    return commit_info

def get_user_info(commit_info):
    user_info = []
    user_info.append('User: ywang567')

    return user_info + commit_info


if __name__ == '__main__':
    repo_info = get_repo_info()
    commit_info = get_commit_info(repo_info);
    for entry in get_user_info(commit_info):
        print(entry)
