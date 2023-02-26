*** Settings ***
Library    SeleniumLibrary
Test Setup  Open Wikipedia
Test Teardown  Screenshot and Close

*** Variables ***
${wikipedia_login}    RobotTests
${wikipedia_password}    RobotFramework
${error_message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***
Open Wikipedia
    Open Browser  https://pl.wikipedia.org/  chrome

Screenshot and Close
    capture page screenshot
    close browser

Log in Wikipedia
    [Arguments]  ${login}   ${password}
    Click Element  id:pt-login
    ${my_value}  get text    id:wpName1
    should be empty  ${my_value}
    Input Text  id:wpName1  ${login}
    Clear Element Text  id:wpPassword1
    input password  id:wpPassword1  ${password}
    checkbox should not be selected  wpRemember
    select checkbox  wpRemember
    checkbox should be selected  wpRemember
    click button  id:wpLoginAttempt
*** Test Cases ***
Successful login to Wikipedia
        Log in Wikipedia    ${wikipedia_login}    ${wikipedia_password}
#        location should be


Unsuccessful login to Wikipedia
        Log in Wikipedia    ${wikipedia_login}    abcd
        wait until element is visible    //*[@id="userloginForm"]/form/div[1]    3s
        ${current_error_message}    get text    //*[@id="userloginForm"]/form/div[1]
        log    ${current_error_message}
        log to console  ${current_error_message}
        Should Be Equal As Strings    ${current_error_message}    ${error_message}
#        capture page screenshot
#        close browser

Search in Wikipedia - wroclaw
#    Open Browser  https://pl.wikipedia.org/  chrome
#    Click Element  id:pt-login
#    Input Text  id:wpName1  ${wikipedia_login}
#    input password  id:wpPassword1  ${wikipedia_password}
#    checkbox should not be selected  wpRemember
#    select checkbox  wpRemember
#    checkbox should be selected  wpRemember
#    click button  id:wpLoginAttempt
    Log in Wikipedia    ${wikipedia_login}    ${wikipedia_password}
    Input Text     id:searchInput  wroclaw
    click button  id:searchButton
    sleep  2s
#    close browser

Search in Wikipedia - Border Colie
    Log in Wikipedia    ${wikipedia_login}    ${wikipedia_password}
    Input Text     id:searchInput  Border Colie
    click button  id:searchButton
    sleep  2s
#    close browser

