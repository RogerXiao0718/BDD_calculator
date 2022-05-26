# -- FILE: features/example.feature
Feature: Commutative operations
  As a student of primary school
  In order to finish my homework
  I want to do arithmetic operations

  Scenario: satisfy commutative property1
    When I enter "3 + 4" first
    And I enter "4 + 3" again
    Then I get the same answer

  Scenario: satisfy commutative property2
    When I enter "2 * 5" first
    And I enter "5 * 2" again
    Then I get the same answer

  