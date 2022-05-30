# -- FILE: features/example.feature
Feature: Commutative operations
  As a student of primary school
  In order to finish my homework
  I want to do arithmetic operations

  Scenario: satisfy commutative property
    When I enter <expression1> first
    And I enter <expression2> again
    Then I get the same answer
    Examples:
    | expression1 | expression2 |
    | 3 + 4       | 4 + 3       |
    | 2 * 5       | 5 * 2       |


  