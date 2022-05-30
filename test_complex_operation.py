from operator import and_
from pytest_bdd import scenarios, given, then, when, parsers
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

scenarios('./features/commutative_operation.feature')
scenarios('./features/associative_operation.feature')
scenarios('./features/distribution_operation.feature')

CALCULATOR_HOME = 'localhost:5000/'

@pytest.fixture()
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    b.get(CALCULATOR_HOME)
    yield b

@pytest.fixture()
def operation_cache():
    yield {}

@when(parsers.parse('I enter {expression1} first'))
def enter_expression1(browser, operation_cache, expression1):
    expression_input = browser.find_element_by_name('expression')
    expression_input.send_keys(expression1)
    browser.find_element_by_name('calculate').click()
    browser_answer = browser.find_element_by_id('ans-txt').get_attribute('innerHTML')
    operation_cache["result1"] = browser_answer
    expression_input.clear()


@when(parsers.parse('I enter {expression2} again'))
def click_equal_button(browser, operation_cache, expression2):
    expression_input = browser.find_element_by_name('expression')
    expression_input.send_keys(expression2)
    browser.find_element_by_name('calculate').click()
    browser_answer = browser.find_element_by_id('ans-txt').get_attribute('innerHTML')
    operation_cache["result2"] = browser_answer
    expression_input.clear()


@then(parsers.parse('I get the same answer'))
def calc_result(browser, operation_cache):
    assert operation_cache["result1"] == operation_cache["result2"]
    browser.quit()