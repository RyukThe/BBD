Feature: Login

Scenario: User should able to login by using valid crendiatls.
Given Launch Browser
And hit URL https://admin-demo.nopcommerce.com/
When Enter Email id: admin@yourstore.com and password: admin
And Capture Title of Login Page
And Click on login button 
Then Home page title
And click on logout button 