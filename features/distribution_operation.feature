# -- FILE: features/example.feature
Feature: Distributive operations
  As a student of primary school
  In order to finish my homework
  I want to do arithmetic operations

  Scenario: satisfy commutative property1
    When I enter "2 * (1 + 3)" first
    And I enter "(2 * 1) + (2 * 3)" again
    Then I get the same answer

  Scenario: satisfy commutative property2
    When I enter "(1 + 3) * 2" first
    And I enter "(1 * 2) + (3 * 2)" again
    Then I get the same answer

  