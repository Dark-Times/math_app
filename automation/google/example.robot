*** Settings ***
Resource  resource.robot
Test Tags  smoke

*** Test Cases ***
Search for a cat
    [Tags]  test_case_id:12345  severity:blocker
    Open Browser To Search Page
    Perform Search    cat
    [Teardown]  Close Browser

Search for a dog
    [Tags]  test_case_id:54321  severity:normal
    Open Browser To Search Page
    Perform Search    dog
    [Teardown]  Close Browser