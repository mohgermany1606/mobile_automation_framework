from selenium.webdriver.common.by import By

class HomePageLocators:
    EDITBOX_ID = (By.ID, "editbox_id")
    START_IDENT_BUTTON = (By.ID, "start_ident_button")

class TermsConditionsLocators:
    CLOSE_ICON = (By.ID, "close_icon")

class ReasonsPageLocators:
    REASONS_OPTIONS = (By.ID, "reasons_options")
    QUIT_SESSION_BUTTON = (By.ID, "quit_session_button")

class IntermediatePageLocators:
    INTERMEDIATE_SCREEN = (By.ID, "intermediate_screen")
