import yaml
from testpage import OperationsHelper
from TestAPI import HelperAPI
import time
import random, string
import logging

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test 1 start')
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pswd('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step2(browser):
    logging.info('Test 2 start')
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pswd(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_login_text() == 'Blog'


def test_step3(browser):
    logging.info('Test 3 start')
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.click_new_post_button()
    testpage.enter_title_post('I want drink!')
    testpage.enter_description_post('Vodka')
    testpage.enter_content_post("".join(random.choices(string.ascii_lowercase + string.digits, k=300)))
    testpage.click_save_new_post_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.check_exist_post() == 'I want drink!'


def test_step4(browser):
    logging.info('Test 4 start')
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.click_contactus_button()
    testpage.enter_name_field("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))
    testpage.enter_email_field(testdata['test_email'])
    testpage.enter_content_field("".join(random.choices(string.ascii_lowercase + string.digits, k=200)))
    testpage.click_contactus_send_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.text_alert() == 'Form successfully submitted'


def test_api_step5(token):
    logging.info('Test 5 start')
    test_api = HelperAPI()
    test_api.create_post_api(token)
    result = test_api.get_my_post(token)
    description_list = test_api.check_description(result)
    assert testdata['description'] in description_list


def test_api_step6(token):
    logging.info('Test 6 start')
    test_api = HelperAPI()
    result = test_api.get_not_my_posts(token)
    title_list = test_api.check_title(result)
    assert testdata['not_my_title'] in title_list and testdata['title'] not in title_list
