#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then, step
import requests

global_general_variables = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}


@given(u'Set basic web application url is "{basic_app_url}"')
def step_impl(context, basic_app_url):
    global_general_variables['basic_application_URL'] = basic_app_url


@given(u'Set basic user details as "{particular}" and "{value}" below')
def step_impl(context, particular, value):
    for row in context.table:
        temp_value = row['value']
        global_general_variables[row['particular']] = temp_value
        if 'empty' in temp_value:
            global_general_variables[row['particular']] = ''


@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type


@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type


@given(u'Set GET api endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] = get_api_endpoint


@given(u'Set POST api endpoint as "{post_api_endpoint}"')
def step_impl(context, post_api_endpoint):
    global_general_variables['POST_api_endpoint'] = post_api_endpoint


@when(u'Set PUT api endpoint as "{put_api_endpoint}"')
def step_impl(context, put_api_endpoint):
    global_general_variables['PUT_api_endpoint'] = put_api_endpoint


@when(u'Set DELETE api endpoint as "{delete_api_endpoint}"')
def step_impl(context, delete_api_endpoint):
    global_general_variables['DELETE_api_endpoint'] = delete_api_endpoint


@when(u'Set Query param as "{query_param}"')
def step_impl(context, query_param):
    if 'empty' in query_param:
        http_request_url_query_param.clear()
    else:
        http_request_url_query_param.clear()
        http_request_url_query_param['signout_emailid'] = global_general_variables['email']
        http_request_url_query_param['session_id'] = global_general_variables['latest_session_key']


@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = global_general_variables['basic_application_URL']
    if 'GET' == http_request_type:
        url_temp += global_general_variables['GET_api_endpoint']
        http_request_body.clear()
        global_general_variables['response_full'] = requests.get(url_temp,
                                                                                         headers=http_request_header,
                                                                                         params=http_request_url_query_param,
                                                                                         data=http_request_body)
    elif 'POST' == http_request_type:
        url_temp += global_general_variables['POST_api_endpoint']
        http_request_url_query_param.clear()
        global_general_variables['response_full'] = requests.post(url_temp,
                                                                                         headers=http_request_header,
                                                                                         params=http_request_url_query_param,
                                                                                         data=http_request_body)
    elif 'PUT' == http_request_type:
        url_temp += global_general_variables['PUT_api_endpoint']
        http_request_url_query_param.clear()
        global_general_variables['response_full'] = requests.put(url_temp,
                                                                                         headers=http_request_header,
                                                                                         params=http_request_url_query_param,
                                                                                         data=http_request_body)
    elif 'DELETE' == http_request_type:
        url_temp += global_general_variables['DELETE_api_endpoint']
        http_request_body.clear()
        global_general_variables['response_full'] = requests.delete(url_temp,
                                                                                            headers=http_request_header,
                                                                                            params=http_request_url_query_param,
                                                                                            data=http_request_body)


@then(u'Valid HTTP response should be received')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, 'Null response received'


@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    global_general_variables['expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['response_full'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    global_general_variables['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = global_general_variables['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@then(u'Response BODY should not be null or empty')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, '***ERROR:  Null or none response body received'


@when(u'Set BODY form param using basic user details')
def step_impl(context):
    http_request_body['signup_emailid'] = global_general_variables['email']
    http_request_body['signup_password'] = global_general_variables['password']
    http_request_body['signup_firstname'] = global_general_variables['first_name']
    http_request_body['signup_lastname'] = global_general_variables['last_name']
    http_request_body['signup_gender'] = global_general_variables['gender']
    http_request_body['signup_secret_question_1'] = global_general_variables['signup_secret_question_1']
    http_request_body['signup_secret_question_2'] = global_general_variables['signup_secret_question_2']
    http_request_body['signup_secret_question_1_answer'] = global_general_variables['signup_secret_question_1_answer']
    http_request_body['signup_secret_question_2_answer'] = global_general_variables['signup_secret_question_2_answer']


@given(u'Perform setup for DELETE request')
def step_impl(context):
    # sign up POST
    global_general_variables['POST_api_endpoint'] = 'signup'
    global_general_variables['email'] = global_general_variables['email'].replace('01','02') #  some random number
    http_request_header['content-type'] = 'application/x-www-form-urlencoded'
    http_request_header['Accept'] = 'application/json'
    http_request_body['signup_emailid'] = global_general_variables['email']
    http_request_body['signup_password'] = global_general_variables['password']
    http_request_body['signup_firstname'] = global_general_variables['first_name']
    http_request_body['signup_lastname'] = global_general_variables['last_name']
    http_request_body['signup_gender'] = global_general_variables['gender']
    http_request_body['signup_secret_question_1'] = global_general_variables['signup_secret_question_1']
    http_request_body['signup_secret_question_2'] = global_general_variables['signup_secret_question_2']
    http_request_body['signup_secret_question_1_answer'] = global_general_variables['signup_secret_question_1_answer']
    http_request_body['signup_secret_question_2_answer'] = global_general_variables['signup_secret_question_2_answer']
    http_request_url_query_param.clear()
    url_temp = global_general_variables['basic_application_URL']
    url_temp += global_general_variables['POST_api_endpoint']
    global_general_variables['response_full'] = requests.post(url_temp,
                                                              headers=http_request_header,
                                                              params=http_request_url_query_param,
                                                              data=http_request_body)
    current_json = global_general_variables['response_full'].json()
    global_general_variables['activation_key'] = current_json['Payload']
    # activate GET
    global_general_variables['ACTIVATE_api_endpoint'] = 'activate'
    http_request_header['content-type'] = 'application/json'
    http_request_header['Accept'] = 'application/json'
    http_request_body.clear()
    http_request_url_query_param.clear()
    http_request_url_query_param['signup_emailid'] = global_general_variables['email']
    http_request_url_query_param['account_basic_activatation_key'] = global_general_variables['activation_key']
    url_temp = global_general_variables['basic_application_URL']
    url_temp += global_general_variables['ACTIVATE_api_endpoint']
    global_general_variables['response_full'] = requests.get(url_temp,
                                                             headers=http_request_header,
                                                             params=http_request_url_query_param,
                                                             data=http_request_body)
    # signin POST
    global_general_variables['SIGNIN_api_endpoint'] = 'signin'
    http_request_header['content-type'] = 'application/x-www-form-urlencoded'
    http_request_header['Accept'] = 'application/json'
    http_request_body.clear()
    http_request_body['signin_emailid'] = global_general_variables['email']
    http_request_body['signin_password'] = global_general_variables['password']
    http_request_url_query_param.clear()
    url_temp = global_general_variables['basic_application_URL']
    url_temp += global_general_variables['SIGNIN_api_endpoint']
    global_general_variables['response_full'] = requests.post(url_temp,
                                                              headers=http_request_header,
                                                              params=http_request_url_query_param,
                                                              data=http_request_body)
    current_json = global_general_variables['response_full'].json()
    global_general_variables['latest_session_key'] = current_json['Payload']


@given(u'Perform setup for PUT request')
def step_impl(context):
    # sign up POST
    global_general_variables['POST_api_endpoint'] = 'signup'
    global_general_variables['email'] = global_general_variables['email'].replace('01','03') #  some random number
    http_request_header['content-type'] = 'application/x-www-form-urlencoded'
    http_request_header['Accept'] = 'application/json'
    http_request_body['signup_emailid'] = global_general_variables['email']
    http_request_body['signup_password'] = global_general_variables['password']
    http_request_body['signup_firstname'] = global_general_variables['first_name']
    http_request_body['signup_lastname'] = global_general_variables['last_name']
    http_request_body['signup_gender'] = global_general_variables['gender']
    http_request_body['signup_secret_question_1'] = global_general_variables['signup_secret_question_1']
    http_request_body['signup_secret_question_2'] = global_general_variables['signup_secret_question_2']
    http_request_body['signup_secret_question_1_answer'] = global_general_variables['signup_secret_question_1_answer']
    http_request_body['signup_secret_question_2_answer'] = global_general_variables['signup_secret_question_2_answer']
    http_request_url_query_param.clear()
    url_temp = global_general_variables['basic_application_URL']
    url_temp += global_general_variables['POST_api_endpoint']
    global_general_variables['response_full'] = requests.post(url_temp,
                                                              headers=http_request_header,
                                                              params=http_request_url_query_param,
                                                              data=http_request_body)
    current_json = global_general_variables['response_full'].json()
    global_general_variables['activation_key'] = current_json['Payload']
    # activate GET
    global_general_variables['ACTIVATE_api_endpoint'] = 'activate'
    http_request_header['content-type'] = 'application/json'
    http_request_header['Accept'] = 'application/json'
    http_request_body.clear()
    http_request_url_query_param.clear()
    http_request_url_query_param['signup_emailid'] = global_general_variables['email']
    http_request_url_query_param['account_basic_activatation_key'] = global_general_variables['activation_key']
    url_temp = global_general_variables['basic_application_URL']
    url_temp += global_general_variables['ACTIVATE_api_endpoint']
    global_general_variables['response_full'] = requests.get(url_temp,
                                                             headers=http_request_header,
                                                             params=http_request_url_query_param,
                                                             data=http_request_body)
    # signin POST
    global_general_variables['SIGNIN_api_endpoint'] = 'signin'
    http_request_header['content-type'] = 'application/x-www-form-urlencoded'
    http_request_header['Accept'] = 'application/json'
    http_request_body.clear()
    http_request_body['signin_emailid'] = global_general_variables['email']
    http_request_body['signin_password'] = global_general_variables['password']
    http_request_url_query_param.clear()
    url_temp = global_general_variables['basic_application_URL']
    url_temp += global_general_variables['SIGNIN_api_endpoint']
    global_general_variables['response_full'] = requests.post(url_temp,
                                                              headers=http_request_header,
                                                              params=http_request_url_query_param,
                                                              data=http_request_body)
    current_json = global_general_variables['response_full'].json()
    global_general_variables['latest_session_key'] = current_json['Payload']
    #   basic_account_profile_details GET
    global_general_variables['GET_ACCOUNT_PROFILE_DETAILS_api_endpoint'] = 'get_account_profile_details'
    http_request_header['content-type'] = 'application/json'
    http_request_header['Accept'] = 'application/json'
    http_request_body.clear()
    http_request_url_query_param.clear()
    http_request_url_query_param['signin_emailid'] = global_general_variables['email']
    http_request_url_query_param['signin_password'] = global_general_variables['password']
    http_request_url_query_param['latest_session_key'] = global_general_variables['latest_session_key']
    url_temp = global_general_variables['basic_application_URL']
    url_temp += global_general_variables['GET_ACCOUNT_PROFILE_DETAILS_api_endpoint']
    global_general_variables['response_full'] = requests.get(url_temp,
                                                              headers=http_request_header,
                                                              params=http_request_url_query_param,
                                                              data=http_request_body)


@when(u'Modify BODY form param first name as "{new_first_name}" and last name as "{new_last_name}"')
def step_impl(context, new_first_name, new_last_name):
    http_request_body['signin_firstname'] = new_first_name
    http_request_body['signin_lastname'] = new_last_name
    http_request_body['signin_emailid'] = global_general_variables['email']
    http_request_body['signin_password'] = global_general_variables['password']
    http_request_body['signin_gender'] = global_general_variables['gender']
    http_request_body['latest_session_key'] = global_general_variables['latest_session_key']


@then(u'Response BODY parsing for "{body_parsing_for}" should be successful')
def step_impl(context, body_parsing_for):
    current_json = global_general_variables['response_full'].json()
    if 'GET__signup' == body_parsing_for:
       print('Activity status               : ' + current_json['Additional message'])
       print('Additional message      : ' + current_json['Activity status'])
       print('Links                               : ')
       print('          Actual signup                                          : ' + current_json['Links'].get('Actual signup'))
       print('          Link documentation                               : ' + current_json['Links'].get('Actual signup'))
       print('Payload                          : ')
       print('          signup_emailid                                       : ' + current_json['Payload'].get('signup_emailid'))
       print('          signup_password                                   : ' + current_json['Payload'].get('signup_password'))
       print('          signup_firstname                                   : ' + current_json['Payload'].get('signup_firstname'))
       print('          signup_lastname                                    : ' + current_json['Payload'].get('signup_lastname'))
       print('          signup_gender                                       : ' + current_json['Payload'].get('signup_gender'))
       print('          signup_secret_question_1                   : ' + current_json['Payload'].get('signup_secret_question_1'))
       print('          signup_secret_question_2                   : ' + current_json['Payload'].get('signup_secret_question_2'))
       print('          signup_secret_question_1_answer    : ' + current_json['Payload'].get('signup_secret_question_1_answer'))
       print('          signup_secret_question_2_answer    : ' + current_json['Payload'].get('signup_secret_question_2_answer'))
    elif 'POST__signup' == body_parsing_for:
       print('Activity status               : ' + current_json['Additional message'])
       print('Additional message      : ' + current_json['Activity status'])
       global_general_variables['activation_key'] = current_json['Payload']
       print('Payload  or activation key                         :\n' + global_general_variables['activation_key'])
    elif 'PUT__modify_account_profile_details' == body_parsing_for:
        print('Activity status               : ' + current_json['Additional message'])
        print('Additional message      : ' + current_json['Activity status'])
        print('Payload                          : ' + current_json['Payload'])
    elif 'DELETE__signout' == body_parsing_for:
        print('Activity status               : ' + current_json['Additional message'])
        print('Additional message      : ' + current_json['Activity status'])
        print('Payload                          : ' + current_json['Payload'])
        global_general_variables['session id'] = ''
