import time


class Home_page:

    URL = 'https://www.makemytrip.com/'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        time.sleep(5)



