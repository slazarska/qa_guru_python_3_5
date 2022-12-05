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
    browser.element('#react-select-3-input').press_tab()

    browser.element('#city').click()
    browser.element('#react-select-4-input').press_enter()

    #метод click() selena не работает, error message 'element click intercepted: Element <button id="submit"...">...</button> is not clickable at point (1377, 863).
    #если бы элемент становился кликабельным после заполнения обязательных полей, можно было бы
    #добавить проверку изменения состояния элемента до и после заполнения формы
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts('Test Firstname Testlastname',
                                                                       'testemailaddress@testmailservice.com',
                                                                       'Other',
                                                                       '9211234567',
                                                                       '24 September,1980',
                                                                       'Maths, Computer Science',
                                                                       'Sports, Reading, Music',
                                                                       'testuserpic.jpg',
                                                                       'Test st., 123, 45',
                                                                       'Uttar Pradesh Agra'))