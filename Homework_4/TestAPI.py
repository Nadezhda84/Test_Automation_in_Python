import logging
import requests
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


class HelperAPI:
    def __init__(self):
        self.base_url = 'https://test-stand.gb.ru/'

    def create_post_api(self, token):
        try:
            requests.post(url=self.base_url + testdata['post'], headers={'X-Auth-Token': token},
                          params={"title": testdata['title'],
                                  'description': testdata['description'],
                                  'content': testdata['content']})
            return True
        except:
            logging.exception('Exception with create post')
            return False

    def get_my_post(self, token):
        try:
            res_get = requests.get(url=self.base_url + testdata['post'], headers={'X-Auth-Token': token},
                                   params={'owner': 'Me'})
            return res_get
        except:
            logging.exception('Exception with request')
            return None

    def check_description(self, result):
        try:
            description_list = [i['description'] for i in result.json()['data']]
            return description_list
        except:
            logging.exception('Exception with description_list')
            return None

    def get_not_my_posts(self, token):
        try:
            res_get = requests.get(url=self.base_url + testdata['post'], headers={'X-Auth-Token': token},
                                   params={'owner': 'notMe'})
            print(res_get)
            return res_get
        except:
            logging.exception('Exception with get tittle list')
            return None

    def check_title(self, result):
        try:
            title_list = [i['title'] for i in result.json()['data']]
            return title_list
        except:
            logging.exception('Exception with title_list')
            return None
