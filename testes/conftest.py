import pytest
import selenium.webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    b= selenium.webdriver.Chrome(ChromeDriverManager().install())
    # b.implicity_wait(10)
    yield b

    b.quit()