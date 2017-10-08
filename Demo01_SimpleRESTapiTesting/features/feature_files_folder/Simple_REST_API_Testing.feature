Feature: REST API testing framework using Java REST Assured or JayWay Libraries 
	Raise request(s) using REST Assured library
	Validate HTTP response code and parse JSON response using REST Assured library
	Make sure to run the intended REST API based web application as pre-condition

Background: 
	Given Set basic web application url is "http://localhost:8080/imademethink/restfulapi/account_basic/"
	  And Set basic user details as "<particular>" and "<value>" below
		| particular                                      | value                                                  |
		| email                                             | Kuppy01@aaa.com                             |
		| password                                      | k9aPass                                             |
		| first_name                                     | Sheldon                                             |
		| last_name                                     | Cooper                                               |
		| gender                                          | m                                                       |
		| signup_secret_question_1              | What is the brand of your toothpaste   |
		| signup_secret_question_2              | What was the name of your babysitter |
		| signup_secret_question_1_answer | Pune                                                  |
		| signup_secret_question_2_answer | Toystory                                             |
		| session id                                      | empty                                                 |

Scenario: GET request example
  Given Set GET api endpoint as "signup"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json" 
	And Set Query param as "empty" 
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200 
	And Response HEADER content type should be "application/json" 
	And Response BODY should not be null or empty 
	And Response BODY parsing for "GET__signup" should be successful 

Scenario: POST request example
  Given Set POST api endpoint as "signup"
 When Set HEADER param request content type as "application/x-www-form-urlencoded"
	And Set HEADER param response accept type as "application/json" 
	And Set BODY form param using basic user details 
	And Raise "POST" HTTP request 
  Then Valid HTTP response should be received
	And Response http code should be 201 
	And Response HEADER content type should be "application/json" 
	And Response BODY should not be null or empty 
	And Response BODY parsing for "POST__signup" should be successful 

Scenario: PUT request example
  Given Perform setup for PUT request
 When Set PUT api endpoint as "modify_account_profile_details"
	And Set HEADER param request content type as "application/x-www-form-urlencoded" 
	And Set HEADER param response accept type as "application/json" 
	And Set BODY form param using basic user details 
	And Modify BODY form param first name as "Jack" and last name as "Wilson" 
	And Raise "PUT" HTTP request 
  Then Valid HTTP response should be received
	And Response http code should be 200 
	And Response HEADER content type should be "application/json" 
	And Response BODY should not be null or empty 
	And Response BODY parsing for "PUT__modify_account_profile_details" should be successful 

Scenario: DELETE request example
  Given Perform setup for DELETE request
 When Set DELETE api endpoint as "signout"
	And Set HEADER param request content type as "application/json" 
	And Set HEADER param response accept type as "application/json" 
	And Set Query param as "based on user details" 
	And Raise "DELETE" HTTP request 
  Then Valid HTTP response should be received
	And Response http code should be 200 
	And Response HEADER content type should be "application/json" 
	And Response BODY should not be null or empty 
	And Response BODY parsing for "DELETE__signout" should be successful 
