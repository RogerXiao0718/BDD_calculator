# -- FILE: features/example.feature
Feature: Distributive operations
  As a student of primary school
  In order to finish my homework
  I want to do arithmetic operations

  Scenario: satisfy commutative property1
    When I enter <expression1> first
    And I enter <expression2> again
    Then I get the same answer
    Examples:
    | expression1 | expression2   |
    | 2 * (1 + 3) | (2*1) + (2*3) |
    | (1 + 3) * 2 | (1*2) + (3*2) |
  