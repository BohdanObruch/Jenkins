from selene import have, by
from selene.core import command
from selene.support.shared.jquery_style import s
from demoqa_test.controls.utils import resource


class StudentRegistrationForm:

    def set_first_name(self, value):
        s('#firstName').type(value)
        return self

    def set_last_name(self, value):
        s('#lastName').type(value)
        return self

    def set_email(self, value):
        s('#userEmail').type(value)
        return self

    def set_mobile_number(self, value):
        s('#userNumber').type(value)
        return self

    def set_gender(self, value):
        s('#genterWrapper').all('.custom-radio').element_by(have.exact_text(value)).click()
        return self

    def set_birth_date(self, year: int, month: int, day: int):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__year-select').s(f'[value="{year}"]').click()
        s('.react-datepicker__month-select').s(f'[value="{month}"]').click()
        s(f'.react-datepicker__day--00{day}').click()
        return self

    def select_subjects(self, *values):
        for value in values:
            s('#subjectsInput').set_value(value).press_enter()
        return self

    def select_hobbies(self, *values):
        for value in values:
            s('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, file: str):
        s('#uploadPicture').send_keys(resource(file))
        return self

    def set_address(self, value):
        s('#currentAddress').type(value)
        return self

    def set_state_and_city(self, state: str, city: str):
        s('#state').perform(command.js.scroll_into_view).click()
        s(by.text(state)).click()
        s('#city').click()
        s(by.text(city)).click()
        return self

    @staticmethod
    def submit_form():
        s('#submit').perform(command.js.click)
