import pytest


'''
According to https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
By default, any tests using a base URL will be skipped.
This is because all tests are considered destructive
and all environments are considered sensitive. 
'''

@pytest.mark.nondestructive
def test_click(page):
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")


@pytest.mark.nondestructive
def test_load_delay(page):
    page.goto("/loaddelay")
    page.click("text=Load Delay")
    page.click(".btn")

@pytest.mark.nondestructive
def test_input(page):
    page.goto("/textinput")
    page.fill("#newButtonName", 'some name')
    page.click("#updatingButton")
    assert page.inner_text('#updatingButton') == 'some name'

@pytest.mark.nondestructive
def test_scrolling(page):
    page.goto("/scrollbars")
    page.click("#hidingButton")

@pytest.mark.nondestructive
def test_login_fail(page):
    page.goto('/sampleapp')
    page.fill('//input[@placeholder="User Name"]', 'some name')
    page.click('#login')
    assert page.inner_text('#loginstatus') == 'Invalid username/password'

@pytest.mark.nondestructive
def test_login_logout(page):
    page.goto("/sampleapp")
    page.fill('//input[@placeholder="User Name"]', 'some_name')
    page.fill('//input[@name="Password"]', "pwd")
    page.click('#login')
    assert page.inner_text('#loginstatus') == 'Welcome, some_name!'
    # logout
    page.click('#login')
    assert page.inner_text('#loginstatus') == "User logged out."
@pytest.mark.nondestructive
def test_progress_bar(page):
        page.goto("/progressbar")
        page.click("#startButton")
        # it waits for this value to reach 75%
        page.inner_text("#progressBar[aria=valuenow='75']")
        page.click("stopButton")
        assert "Result:0" in page.inner_text("#result")
