import openpyxl
import allure
import pytest
import requests
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import *
import os

def read_credentials_from_excel(file_path):
    credentials = []
    workbook =openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username,password =row
        credentials.append(
            {
                "username":username,
                "password":password
            }
        )
    return credentials

def create_auth_request(username,password):
    payload={
        "username":username,
        "password":password
    }
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload,
        in_json=False
    )
    return response

# @pytest.mark.parametrize("user_cred",read_credentials_from_excel(os.getcwd()+"/testdata_ddt_123.xlsx"))
# def test_create_auth_with_excel(user_cred):
#     print(os.getcwd())
#     # file_path = "C:\\Users\\Dell\\PycharmProjects\\Py3xAPIRestFramework\\tests\\tests\\DataDrivenTesting\\testdata_ddt_123.xlsx"
#     # credentials = read_credentials_from_excel(file_path=file_path)
#     # print(credentials)
#     # for user_cred in credentials:
#     username =user_cred["username"]
#     password = user_cred["password"]
#     print(username,password)
#     response = create_auth_request(username=username,password=password)
#     print(response.status_code)

def test_create_auth_with_excel_using_for_loop():
    file_path = os.getcwd()+"/testdata_ddt_123.xlsx"
    credentials = read_credentials_from_excel(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username =user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response = create_auth_request(username=username,password=password)
        print(response.status_code)
