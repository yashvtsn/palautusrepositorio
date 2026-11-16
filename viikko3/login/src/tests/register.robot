*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  antti
    Set Password  12345678
    Set Password Confirmation  12345678
    Get Property  id=password_confirmation  value  ==  12345678
    Click  button >> text=Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  12345678
    Set Password Confirmation  12345678
    Click  button >> text=Register
    Registration Should Fail With Message  Invalid username or password

Register With Valid Username And Too Short Password
    Set Username  antti
    Set Password  123
    Set Password Confirmation  123
    Click  button >> text=Register
    Registration Should Fail With Message  Invalid username or password

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  12345678
    Set Password Confirmation  12345678
    Click  button >> text=Register
    Registration Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page