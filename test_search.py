import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def open_browser():
    browser.open('https://google.com/ncr')

@pytest.fixture()
def size_browser():
    browser.config.window_height = 900
    browser.config.window_width = 1600

def test_search_selene(open_browser, size_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Tests with Selene can be built either in a simple straightforward'))

def test_search_abcde(open_browser, size_browser):
    browser.element('[name="q"]').should(be.blank).type('trdfgvdfdzrgzdr').press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results '))
    print('Поиск не дал результатов')