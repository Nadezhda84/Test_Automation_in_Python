import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(site, selector_log, selector_pass,
               selector_button, selector_err):

    input1 = site.find_element("xpath", selector_log)
    input1.send_keys("test")
    input2 = site.find_element("xpath", selector_pass)
    input2.send_keys("test")
    btn = site.find_element("xpath", selector_button)
    btn.click()
    err_label = site.find_element("xpath", selector_err)
    assert err_label.text == "401"


def test_step2(site, selector_log, selector_pass,
               selector_button, res_authorisation):
    input1 = site.find_element("xpath", selector_log)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", selector_pass)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", selector_button)
    btn.click()
    authorisation = site.find_element("xpath", res_authorisation)
    assert authorisation.text == "Home"


def test_step3(site, selector_log, selector_pass,
               selector_button, new_post, input_title,
               input_description,
               input_content, selector_button2, post_title):
    input1 = site.find_element("xpath", selector_log)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", selector_pass)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", selector_button)
    btn.click()
    post = site.find_element("xpath", new_post)
    post.click()
    input3 = site.find_element("xpath", input_title)
    input3.send_keys(testdata["title"])
    input4 = site.find_element("xpath", input_description)
    input4.send_keys(testdata["description"])
    input5 = site.find_element("xpath", input_content)
    input5.send_keys(testdata["content"])
    btn2 = site.find_element("xpath", selector_button2)
    btn2.click()
    p_title = site.find_element("xpath", post_title)
    assert p_title.text == testdata["title"]