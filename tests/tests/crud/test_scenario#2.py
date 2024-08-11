# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it
# should not exist.
import logging

import allure


from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

class Test_delete_get_Booking(object):
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_updatepartial_booking(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        header = Utils().common_header_put_delete_patch_cookie(token=token)
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        print(delete_url)
        book = booking_id
        print(book)
        response = delete_requests(
            url=delete_url,
            headers=header,
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=201)

        # res = get_request(
        #     url=APIConstants.url_patch_put_delete(booking_id=book),
        #     headers=header,
        #     auth=None
        # )
        # print(delete_url)
        # verify_http_status_code(response_data=res, expect_data=404)