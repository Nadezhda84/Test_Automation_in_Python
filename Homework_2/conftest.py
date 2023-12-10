import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def selector_log():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture()
def selector_pass():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture()
def selector_button():
    return '//*[@id="login"]/div[3]'


@pytest.fixture()
def selector_err():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture()
def res_authorisation():
    return '//*[@id="app"]/main/nav/a'



@pytest.fixture()
def new_post():
    return '//*[@id="create-btn"]'


@pytest.fixture()
def input_title():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


@pytest.fixture()
def input_description():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'


@pytest.fixture()
def input_content():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'


@pytest.fixture()
def selector_button2():
    return '//*[@id="create-item"]/div/div/div[7]/div/button'


@pytest.fixture()
def post_title():
    return '//*[@id="app"]/main/div/div[1]/h1'



@pytest.fixture()
def site():
    my_site = Site(testdata["address"])
    yield my_site
    my_site.close()