from pages.home import Home_page

def test_home_page(browser):
    home_object = Home_page(browser)
    home_object.load()

