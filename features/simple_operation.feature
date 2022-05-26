# -- FILE: features/example.feature
Feature: Simple operations
  As a student of primary school
  In order to finish my homework
  I want to do arithmetic operations

  Scenario: Do 2 + 3 mathematical calculation
    Given I enter "2 + 3"

    When I press "=" button
    Then I get the answer "5"

  Scenario: Do 3 - 2 mathematical calculation
    Given I enter "3 - 2"

    When I press "=" button
    Then I get the answer "1"

  Scenario: Do 3 * 2 mathematical calculation
    Given I enter "3 * 2"

    When I press "=" button
    Then I get the answer "6"

  Scenario: Do 3 / 2 mathematical calculation
    Given I enter "3 / 2"

    When I press "=" button
    Then I get the answer "1.5"

  Scenario: Do 3 +-*/ 2 mathematical calculation
    Given I enter "3 +-*/ 2"

    When I press "=" button
    Then I get the answer "Invalid Input"

  Scenario: Do hello world mathematical calculation
    Given I enter "hello world"

    When I press "=" button
    Then I get the answer "Invalid Input"
