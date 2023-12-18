from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name} ')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_btn(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    # enter text
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pswd(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PSWD_FIELD'], word, description='pswd form')

    def enter_title_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_TITLE'], word, description='title')

    def enter_description_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_DESCRIPTION'], word, description='description')

    def enter_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_CONTENT'], word, description='content')

    def enter_name_field(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_YOU_NAME_FIELD'], word, description='contact name')

    def enter_email_field(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_YOU_EMAIL_FIELD'], word, description='contact mail')

    def enter_content_field(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'], word, description='contact content')

    # click buttons
    def click_login_button(self):
        self.click_btn(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_new_post_button(self):
        self.click_btn(TestSearchLocators.ids['LOCATOR_CREATE_NEW_POST'], description='new post')

    def click_save_new_post_button(self):
        self.click_btn(TestSearchLocators.ids['LOCATOR_SAVE_BTN'], description='save post')

    def click_contactus_button(self):
        self.click_btn(TestSearchLocators.ids['LOCATOR_CONTACTUS_BTN'], description='contact')

    def click_contactus_send_button(self):
        self.click_btn(TestSearchLocators.ids['LOCATOR_CONTACTUS_SEND_BTN'], description='send')

    # get text
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error label')

    def get_login_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_LOGIN_RESULT'], description='result')

    def check_exist_post(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_EXIST_POST'], description='exist post')

    # don't change, we have try-except on low level
    def text_alert(self):
        logging.info('Get alert text')
        text = self.switch_to_alert()
        logging.info(text)
        return text
