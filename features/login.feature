Feature: OrangeHRM Login

    Scenario: Login to OrangeHRM with valid parameters
        Given I open orange HRM Homepage
        When Enter username "admin" and password "admin123"
        And Click in login button
        Then User must validate if display "Dashboard" in the Dashboard page

    Scenario Outline: Login to OrangeHRM with Multiple parameters
        Given I open orange HRM Homepage
        When Enter username "<username>" and password "<password>"
        And Click in login button
        Then User must validate if display "Dashboard" in the Dashboard page

        Examples:
        | username | password |
        | admin    | admin123 |
        | admin123 | admin    |
        | adminxyz | admin123 |
        | admin    | adminxyz |