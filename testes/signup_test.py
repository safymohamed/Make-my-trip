from pages.home import Home_page
from pages.sign_up import sign_up

def test_signup(browser):
    home_object = Home_page(browser)
    signup_object = sign_up(browser)
    valid_email= "safinazmohamed30@gmail.com"

    home_object.load()
    signup_object.login_click()
    signup_object.email(valid_email)
    signup_object.continue_button()