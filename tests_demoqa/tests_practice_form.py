from selene.support.shared import browser
from selene import have
import os


def test_successful_submit_form():
    browser.open('/automation-practice-form').should(have.title('ToolsQA'))

    browser.element('#firstName').set_value('Test Firstname').press_tab()
    browser.element('#firstName').should(have.value('Test Firstname'))

    browser.element('#lastName').set_value('Testlastname').press_tab()
    browser.element('#lastName').should(have.value('Testlastname'))

    browser.element('#userEmail').set_value('testemailaddress@testmailservice.com').press_tab()
    browser.element('#userEmail').should(have.value('testemailaddress@testmailservice.com'))

    browser.element('[for="gender-radio-1"]').click()
    # если бы у элемента после выбора менялся статус, напр., selected,
    # можно было бы добавить проверку, что после клика элемент выбран +
    # проверку, что выбрано только одно значение гендера
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[for="gender-radio-3"]').click()

    browser.element('#userNumber').set_value('9211234567').press_tab()
    browser.element('#userNumber').should(have.value('9211234567'))

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="1980"]').click()
    browser.element('.react-datepicker__month-select>[value="8"]').click()
    browser.element('.react-datepicker__day--024').click()
    browser.element('#dateOfBirthInput').should(have.value('24 Sep 1980'))

    browser.element('#subjectsInput').set_value('Maths').press_enter()
    browser.element('#subjectsInput').set_value('Computer Science').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()
    # если бы у элемента после выбора менялся статус, напр., selected,
    # можно было бы добавить проверку, что после клика элемент выбран +
    # проверку, что можно выбрать несколько значений хобби
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/images/testuserpic.jpg'))

    browser.element('#currentAddress').type('Test st., 123, 45').press_tab()
    browser.element('#currentAddress').should(have.value('Test st., 123, 45'))

    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()

    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element("//td[text()='Student Name']").element("//td[text()='Test Firstname Testlastname']").should(have.text('Test Firstname Testlastname'))
    browser.element("//td[text()='Student Email']").element("//td[text()='testemailaddress@testmailservice.com']").should(have.text('testemailaddress@testmailservice.com'))
    browser.element("//td[text()='Gender']").element("//td[text()='Other']").should(have.text('Other'))
    browser.element("//td[text()='Mobile']").element("//td[text()='9211234567']").should(have.text('9211234567'))
    browser.element("//td[text()='Date of Birth']").element("//td[text()='24 September,1980']").should(have.text('24 September,1980'))
    browser.element("//td[text()='Subjects']").element("//td[text()='Maths, Computer Science']").should(have.text('Maths, Computer Science'))
    browser.element("//td[text()='Hobbies']").element("//td[text()='Sports, Reading, Music']").should(have.text('Sports, Reading, Music'))
    browser.element("//td[text()='Picture']").element("//td[text()='testuserpic.jpg']").should(have.text('testuserpic.jpg'))
    browser.element("//td[text()='Address']").element("//td[text()='Test st., 123, 45']").should(
        have.text('Test st., 123, 45'))
    browser.element("//td[text()='State and City']").element("//td[text()='NCR Delhi']").should(
        have.text('NCR Delhi'))