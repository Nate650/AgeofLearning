import time

from .common import Common


class SignUp(Common):
    JS_PATH_SIGN_UP_BUTTON = 'return document.querySelector("body > route-view").shadowRoot.querySelector("#page-component").shadowRoot.querySelector("main-layout > header > home-header > authstate-context:nth-child(3) > signup-button")'
    JS_PATH_EMAIL = 'return document.querySelector("body > route-view").shadowRoot.querySelector("#page-component").shadowRoot.querySelector("#email")'
    JS_PATH_SUBMIT_BUTTON = 'return document.querySelector("body > route-view").shadowRoot.querySelector("#page-component").shadowRoot.querySelector("#submit-button")'
    JS_PATH_BECOME_A_MEMBER_TEXT = 'return document.querySelector("body > route-view").shadowRoot.querySelector("#page-component").shadowRoot.querySelector("#become-member")'
    JS_PATH_EMAIL_FIELD_VALUE = 'return document.querySelector("body > route-view").shadowRoot.querySelector("#page-component").shadowRoot.querySelector("#email-input")'

    def click_sign_up_button(self):
        sign_up_button = self.driver.execute_script(self.JS_PATH_SIGN_UP_BUTTON)
        sign_up_button.click()

    def enter_email_address(self, email):
        email_field = self.driver.execute_script(self.JS_PATH_EMAIL)
        email_field.send_keys(email)

    def click_submit_button(self):
        submit_button = self.driver.execute_script(self.JS_PATH_SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(3)

    def get_become_a_member_text(self):
        return self.driver.execute_script(self.JS_PATH_BECOME_A_MEMBER_TEXT).text

    def get_email_field_value(self):
        email_field = self.driver.execute_script(self.JS_PATH_EMAIL_FIELD_VALUE)
        return email_field.get_attribute("value")
