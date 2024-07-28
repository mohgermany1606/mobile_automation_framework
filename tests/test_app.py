import unittest
from appium.webdriver.common.appiumby import AppiumBy
from utils.driver import get_driver

class MobileAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver('ios', 'virtual')  # Specify 'real' for real device tests

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_app_flow(self):
        driver = self.driver

        # Validate that the home screen is displayed
        home_screen_element = driver.find_element(AppiumBy.ID, "home_screen_edit_box")
        self.assertIsNotNone(home_screen_element, "Home screen edit box not found")
        start_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "start_ident_button")
        self.assertIsNotNone(start_button, "Start ident button not found")

        # Enter one of the ident ids and click the start button
        ident_ids = ["TS2-LJGCD", "TS2-QTTUF", "TS2-XKPSF", "TS2-TUHYJ", "TS2-FGAKW", "TS2-AGJGU", "TS2-JRSQV", "TS2-WEKGG", "TS2-RWQBS", "TS2-DWUMM"]
        ident_id = ident_ids[0]
        home_screen_element.send_keys(ident_id)
        start_button.click()

        # Validate that the terms and conditions screen is displayed
        terms_screen_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "terms_and_conditions")
        self.assertIsNotNone(terms_screen_element, "Terms and conditions screen not found")

        # Click on the close icon on the top left corner
        close_icon = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "close_icon")
        close_icon.click()

        # Validate the options with reasons are displayed
        options_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "options_with_reasons")
        self.assertIsNotNone(options_element, "Options with reasons not found")

        # Choose any of the options and click Quit session
        quit_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "quit_option")
        quit_option.click()

        # Validate that there is an intermediate screen displayed before the app redirects to the home screen
        intermediate_screen_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "intermediate_screen")
        self.assertIsNotNone(intermediate_screen_element, "Intermediate screen not found")

if __name__ == '__main__':
    unittest.main()
