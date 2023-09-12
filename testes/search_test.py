import time
from pages.search import search
from pages.home import Home_page

def test_search(browser):
    home_object = Home_page(browser)
    search_object = search(browser)
    phrase_from = "New York"
    phrase_to = "cairo"
    Month_departure = "December 2023"
    Month_Return = "Thu Feb 15 2024"
    PHRASE= "Depart Fri, 13 Oct • EgyptAir"


    home_object.load()
    search_object.from_click()
    search_object.flight_from(phrase_from)
    search_object.country_from()
    search_object.to_click()
    search_object.flight_to(phrase_to)
    search_object.country_to()
    search_object.departure_choose(Month_departure)
    search_object.return_click()
    search_object.return_choose(Month_Return)
    search_object.search_button()
    titles = search_object.result_link_title()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0







