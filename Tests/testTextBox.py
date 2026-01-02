from playwright.sync_api import sync_playwright,Page,expect,Browser
from Pages.TextBox import TextBox
import pytest
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

@pytest.mark.parametrize(pu.test_input_data_fields('./Data/textBox.csv'),pu.test_actual_data_values('./Data/textBox.csv'),ids=pu.test_ids_name('./Data/textBox.csv'))
def testTextBox(browser_fixtures,uName,email,caddress,paddress):
        page = browser_fixtures.new_page()
        page.goto('https://demoqa.com/')
        page.locator("//*[name()='path' and contains(@d,'M16 132h41')]").click()
        page.locator("span").filter(has_text="Text Box").click()
        TextBox_inst1 = TextBox(page)
        is_empty = TextBox_inst1.verifiy_all_details_empty_at_first()
        assert is_empty == True
        if is_empty is True :
            TextBox_inst1.fill_TextBox(uName,email,caddress,paddress)
            assert TextBox_inst1.verifiy_userName_loc.inner_text().split(':')[1] == uName
            assert TextBox_inst1.verifiy_emailAddress_loc.inner_text().split(':')[1] == email
            assert TextBox_inst1.verifiy_CurrentAddress_loc.inner_text().split(':')[1] == caddress
            assert TextBox_inst1.verifiy_permAddress_loc.inner_text().split(':')[1] == paddress
            # TextBox_inst1.verifiyDetails('Ravi Teja','raviteja.solleti@gmail.com','Mahadevapura,Bangalore,560048','Mahadevapura,Bangalore,560048')
        else :
            assert False
        # page.close()
        # browser.close()

def testSample1():
    assert 2 ==2