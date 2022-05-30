from pytest_bdd import scenarios, given, then, when, parsers
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

scenarios('./features/simple_operation.feature')

CALCULATOR_HOME = 'localhost:5000/'

@pytest.fixture()
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    b.get(CALCULATOR_HOME)
    yield b


@given(parsers.parse('I enter {expression}'))
def enter_expression1(browser, expression):
    expression_input = browser.find_element_by_name('expression')
    expression_input.send_keys(expression)


@when(parsers.parse('I press "=" button'))
def click_equal_button(browser):
    calculate_button = browser.find_element_by_name('calculate')
    calculate_button.click()    


@then(parsers.parse('I get the answer {answer}'))
def calc_result(browser, answer):
    browser_answer = browser.find_element_by_id('ans-txt').get_attribute('innerHTML')
    assert browser_answer == answer
    browser.quit()