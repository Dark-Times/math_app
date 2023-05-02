*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}  Firefox
${URL}  https://www.google.com/imghp?tbm=isch
${DELAY}  0

*** Keywords ***
Open Browser To Search Page
    Set Selenium Speed    ${DELAY}
    Open Browser  ${URL}
    Maximize Browser Window
    Search Page Should Be Open
    Click Button    Reject all

Search Page Should Be Open
    Title Should Be    Google Images

Perform Search
    [Arguments]  ${search_statement}
    Input Text    q    ${search_statement}
    Submit Form
    Wait For Condition    return document.readyState == "complete"