from selenium.webdriver.common.by import By

class sign_up:
    username_elemant = (By.ID, 'username')
    login_element = (By.XPATH, '//span[@class="landingSprite myIconWhite"]')
    continue_element = (By.XPATH, '//button[@class="capText font16"]')

    def __init__(self, browser):
        self.browser = browser

    def login_click(self):
        login = self.browser.find_element(*self.login_element)
        self.browser.implicitly_wait(10)
        login.click()

    def email(self, valid_email):
         Email = self.browser.find_element(*self.username_elemant)
         Email_enter = Email.send_keys(valid_email)

    def continue_button(self):
        Continue = self.browser.find_element(*self.continue_element)
        Continue.click()
    
