# This page contains a description of how checks will be done on the super calculator page
from .base_page import BasePage
from locators.locators_super_calculator_page import LocatorsSuperCalculatorPage


class MainPage(BasePage, LocatorsSuperCalculatorPage):
    def should_be_page_title(self):
        title_page = self.get_element(MainPage.PAGE_TITLE).text
        assert "Super Calculator" == title_page, \
            "there is no correct page title"

    def should_be_result_of_adding_numbers(self):
        self.get_element(self.FIRST_NUMBER_FIELD)
        self.smart_send_keys(self.FIRST_NUMBER_FIELD, "8")
        self.get_element(self.SECOND_NUMBER_FIELD)
        self.smart_send_keys(self.SECOND_NUMBER_FIELD, "8")
        self.smart_click(self.BUTTON_GO)
        result_addition = self.get_element(self.RESULT_ADDITION).text
        assert "16" == result_addition, \
            "you got wrong result_addition"

    def history_session_calculator_results(self):
        self.get_element(self.FIRST_NUMBER_FIELD)
        self.smart_send_keys(self.FIRST_NUMBER_FIELD, "16")
        self.get_element(self.OPERATIONS)
        self.smart_click(self.OPERATIONS)
        self.get_element(self.OPERATION_DIVISION)
        self.smart_click(self.OPERATION_DIVISION)
        self.get_element(self.SECOND_NUMBER_FIELD)
        self.smart_send_keys(self.SECOND_NUMBER_FIELD, "4")
        self.smart_click(self.BUTTON_GO)
        result_division = self.get_element(self.RESULT_DIVISION).text
        self.get_element(self.FIRST_NUMBER_FIELD)
        self.smart_send_keys(self.FIRST_NUMBER_FIELD, "4")
        self.get_element(self.OPERATIONS)
        self.smart_click(self.OPERATIONS)
        self.get_element(self.OPERATION_MULTIPLICATION)
        self.smart_click(self.OPERATION_MULTIPLICATION)
        self.get_element(self.SECOND_NUMBER_FIELD)
        self.smart_send_keys(self.SECOND_NUMBER_FIELD, "4")
        self.smart_click(self.BUTTON_GO)
        result_multiplication = self.get_element(self.RESULT_MULTIPLICATION).text
        expression_first_line = self.get_element(self.FIRST_LINE_RESULT).text
        expression_second_line = self.get_element(self.SECOND_LINE_RESULT).text
        assert expression_first_line and expression_second_line is not None, \
            "expressions are none"
        assert "4" == result_division, \
            "you got wrong result_division"
        assert "16" == result_multiplication, \
            "you got wrong result_multiplication"
