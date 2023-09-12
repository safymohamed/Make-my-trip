import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class search:
        from_element = (By.XPATH, '//input[contains(@class, "react-autosuggest__input react-autosuggest__input--open")]')
        from_click_element = (By.XPATH, '//span[@class="lbl_input appendBottom10"]')
        from_country = (By.XPATH, '//span[text() = "New York"]')
        t0_click_element = (By.XPATH, '//span[text() = "To"]')
        to_element = (By.XPATH, '//input[contains(@class, "react-autosuggest__input react-autosuggest__input--open")]')
        to_country = (By.XPATH,'//p[text() = "Cairo, Egypt"]')
        date_element = (By.XPATH, '//div[@class="DayPicker-Day"]')
        next_element = (By.XPATH, '//span[@class="DayPicker-NavButton DayPicker-NavButton--next"]')
        calendar_date=(By.XPATH,'//div[@aria-label="Fri Dec 01 2023"]')
        return_next =(By.XPATH,'//span[@aria-label="Next Month"]')
        return_date =(By.XPATH, '//div[@aria-label="Thu Feb 15 2024"]')
        return_element = (By.XPATH, '//span[text() = "Return"]')
        search_element = (By.XPATH,'//a[text() = "Search"]')
        links_element = (By.ID, 'listing-id')


        def __init__(self, browser):
            self.browser = browser

        def from_click(self):
            click_from = self.browser.find_element(*self.from_click_element)
            self.browser.implicitly_wait(10)
            click_from.click()

        def flight_from(self, phrase_from):
            flight_from = self.browser.find_element(*self.from_element)
            flight_from.send_keys(phrase_from)

        def country_from(self):
             country_from = self.browser.find_element(*self.from_country)
             country_from.click()

        def to_click(self):
            click_to = self.browser.find_element(*self.t0_click_element)
            click_to.click()

        def flight_to(self, phrase_to):
            flight_to = self.browser.find_element(*self.to_element)
            flight_to.send_keys(phrase_to)

        def country_to(self):
            country_to = self.browser.find_element(*self.to_country)
            country_to.click()


        def departure_choose(self, Month_departure):
            nextButtonCalendar=self.browser.find_element(*self.next_element)

            for x in range(2):
                nextButtonCalendar.click()

            choose_departure=self.browser.find_element(*self.calendar_date)
            choose_departure.click()

        def return_click(self):
            click_return = self.browser.find_element(*self.return_element)
            click_return.click()

        def return_choose(self, Month_Return):
            next_Button_Return=self.browser.find_element(*self.return_next)

            for i in range(2):
              next_Button_Return.click()

            choose_return=self.browser.find_element(*self.return_date)
            choose_return.click()

        def search_button(self):
            search_click = self.browser.find_element(*self.search_element)
            search_click.click()
            self.browser.implicitly_wait(30)



        def result_link_title(self):
            links = self.browser.find_elements(*self.links_element)
            titles = [link.text for link in links]
            return titles




























