import time

from pages.sign_up import SignUp
from options import options


def test_sign_up(driver):
    page = SignUp(driver)
    page.click_sign_up_button()
    time.sleep(3)
    assert driver.current_url == 'https://www.abcmouse.com/abc/prospect-register/'
    assert page.get_become_a_member_text() == "Become a Member!"
    page.enter_email_address(options['email'])
    page.click_submit_button()
    time.sleep(3)
    assert page.get_email_field_value() == options['email']
