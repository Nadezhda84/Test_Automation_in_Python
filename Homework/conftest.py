import pytest
import requests
import yaml

with open('config.yaml') as f:
    conf = yaml.safe_load(f)
    url = conf["url"]
    login = conf["login"]
    password = conf["password"]
    url_get = conf["url_get"]
    url_post = conf["url_post"]
    ttl = conf["ttl"]


@pytest.fixture()
def get_token():
    result = requests.post(url=url, data={"username": login,
                                          "password": password})
    print(result.json())
    token = result.json()["token"]
    print(token)
    return token


@pytest.fixture()
def request_get(get_token):
    res_get = requests.get(url=url_get, headers={"X-Auth-Token": get_token},
                           params={"owner": "notMe"})
    print(f"fix{res_get.json()}")
    return res_get.json()


@pytest.fixture()
def request_post(get_token):
    res_post = requests.post(url=url_post, headers={"X-Auth-Token": get_token},
                             params={"title": ttl,
                                     "description": "постЭ",
                                     "content": "содержание поста"})
    print(f"fix{res_post.json()}")
    title_post = res_post.json()["title"]
    return title_post