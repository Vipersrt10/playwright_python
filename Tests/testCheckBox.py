from playwright.sync_api import sync_playwright,Page,expect,Browser
from Pages.CheckBox import CheckBox
import pytest
import time
import Utility.param_utility as pu

@pytest.fixture(scope='module',params=['chrome','firefox'])
def browser_fixtures(request):
    with sync_playwright() as p :
        if request.param == 'chrome' :
            browser = p.chromium.launch(headless=False,slow_mo=1000)
            # page = browser.new_page()
        if request.param == 'firefox' :
            browser = p.firefox.launch(headless=False,slow_mo=1000)
            # page = browser.new_page()
        yield browser
        browser.close()

# @pytest.mark.parametrize(pu.test_input_data_fields('./Data/textBox.csv'),pu.test_actual_data_values('./Data/textBox.csv'),ids=pu.test_ids_name('./Data/textBox.csv'))
# ,uName,email,caddress,paddress
def testCheckBoxexpandAll(browser_fixtures):
        page = browser_fixtures.new_page()
        page.goto('https://demoqa.com/')
        page.locator("//*[name()='path' and contains(@d,'M16 132h41')]").click()
        page.locator("span").filter(has_text="Check Box").click()
        CheckBox_inst1 = CheckBox(page)
        CheckBox_inst1.sample_expand()
        # time.sleep(2)
        # CheckBox_inst1.sample_minimize()
        # time.sleep(2)

def testCheckBoxminimizeAll(browser_fixtures):
        page = browser_fixtures.new_page()
        page.goto('https://demoqa.com/')
        page.locator("//*[name()='path' and contains(@d,'M16 132h41')]").click()
        page.locator("span").filter(has_text="Check Box").click()
        CheckBox_inst1 = CheckBox(page)
        CheckBox_inst1.sample_minimize()
        # time.sleep(2)
        # CheckBox_inst1.sample_minimize()
        # time.sleep(2)
        