# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
import logging

import allure


from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

class Test_partial_update_Booking(object):
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_updatepartial_booking(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        header = Utils().common_header_put_delete_patch_cookie(token=token)
        patch_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        print(patch_url)
        response = patch_requests(
            url=patch_url,
            headers=header,
            payload=payload_patch_request(),
            auth=None,
            in_json=False
        )
        verify_response_key(response.json()["firstname"], "Chaitra")
        print(response.content)
        verify_http_status_code(response_data=response, expect_data=200)

