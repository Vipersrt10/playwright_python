from playwright.sync_api import sync_playwright,Page,expect,Browser
from Pages.PracticeForm import practiceForm
import pytest
import Utility.param_utility as pu

@pytest.fixture(scope='module',params=['chrome'])
def browser_fixtures(request):
    with sync_playwright() as p :
        if request.param == 'chrome' :
            browser = p.chromium.launch(headless=False,slow_mo=1000,args=["--start-maximized"])
            # page = browser.new_page()
        if request.param == 'firefox' :
            browser = p.firefox.launch(headless=False,slow_mo=1000,args=["--start-maximized"])
            # page = browser.new_page()
        yield browser
        browser.close()

def testCheckBoxexpandAll(browser_fixtures):
        page = browser_fixtures.new_page()
        page.goto('https://demoqa.com/')
        page.locator("//*[name()='path' and contains(@d,'M16 132h41')]").click()
        page.get_by_text("Forms", exact=True).click()
        page.locator("span").filter(has_text="Practice Form").click()
        page.wait_for_timeout(2000)
        prac_form = practiceForm(page)
        prac_form.fillfirstName('Ravi Teja')
        prac_form.filllastName('Solleti')
        prac_form.filluserEmail('ravsolleti@gmail.com')
        prac_form.fillGender('male')
        prac_form.fillMobileNumber('1234567890')
        prac_form.datePicker()
        prac_form.fillHobbies('all')
        prac_form.fillcurrentAddress('mahadevapura,bangalore')
        prac_form.inputSubject('mat')
        prac_form.inputSubject('scie')
        prac_form.selectState('NCR')
        prac_form.selectcity('Delhi')
        prac_form.submitForm()
        page.wait_for_timeout(5000)
