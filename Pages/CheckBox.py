from playwright.sync_api import Page,Expect,sync_playwright

class CheckBox:
    def __init__(self,page):
        self.page = page
        self.plus_symbol = self.page.locator("//button[@title='Expand all']")
        self.minus_symbol = self.page.locator("//button[@title='Collapse all']")
        self.Desktop_icon = self.page.locator("//span[contains(text(),'Desktop')]")
        self.Home_icon = self.page.locator("//span[contains(text(),'Home')]")
        self.Notes_icon = self.page.locator("//span[contains(text(),'Notes')]")
        self.Commands_icon = self.page.locator("//span[contains(text(),'Commands')]")
        self.Documents_icon = self.page.locator("//span[contains(text(),'Documents')]")
        self.WorkSpace_icon = self.page.locator("//span[contains(text(),'WorkSpace')]")
        self.Office_icon = self.page.locator("//span[contains(text(),'Office')]")
        self.Downloads_icon = self.page.locator("//span[contains(text(),'Downloads')]")
        self.WordFile_icon = self.page.locator("//span[contains(text(),'Word File.doc')]")
        self.ExcelFile_icon = self.page.locator("//span[contains(text(),'Excel File.doc')]")
        self.React_icon = self.page.locator("//span[contains(text(),'React')]")
        self.Angular_icon = self.page.locator("//span[contains(text(),'Angular')]")
        self.Veu_icon = self.page.locator("//span[contains(text(),'Veu')]")
        self.Public_icon = self.page.locator("//span[contains(text(),'Public')]")
        self.Private_icon = self.page.locator("//span[contains(text(),'Private')]")
        self.Classified_icon = self.page.locator("//span[contains(text(),'Classified')]")
        self.General_icon = self.page.locator("//span[contains(text(),'General')]")
    def sample_expand(self):
        self.plus_symbol.click()
        self.page.wait_for_timeout(2000)
        assert self.plus_symbol.is_visible() == True
        assert self.minus_symbol.is_visible() == True
        assert self.Home_icon.is_visible() == True
        assert self.Desktop_icon.is_visible() == True
        assert self.Notes_icon.is_visible() == True
        assert self.Commands_icon.is_visible() == True
        assert self.Documents_icon.is_visible() == True
        assert self.WorkSpace_icon.is_visible() == True
        assert self.React_icon.is_visible() == True
        assert self.Angular_icon.is_visible() == True
        assert self.Veu_icon.is_visible() == True
        assert self.Office_icon.is_visible() == True
        assert self.Public_icon.is_visible() == True
        assert self.Private_icon.is_visible() == True
        assert self.Classified_icon.is_visible() == True
        assert self.General_icon.is_visible() == True
        assert self.Downloads_icon.is_visible() == True
        assert self.WordFile_icon.is_visible() == True
        assert self.ExcelFile_icon.is_visible() == True

    def sample_minimize(self) :
        self.minus_symbol.click()
        self.page.wait_for_timeout(2000)
        assert self.plus_symbol.is_hidden() == False
        assert self.minus_symbol.is_hidden() == False
        assert self.Home_icon.is_hidden() == False
        assert self.Desktop_icon.is_hidden() == True
        assert self.Notes_icon.is_hidden() == True
        assert self.Commands_icon.is_hidden() == True
        assert self.Documents_icon.is_hidden() == True
        assert self.WorkSpace_icon.is_hidden() == True
        assert self.React_icon.is_hidden() == True
        assert self.Angular_icon.is_hidden() == True
        assert self.Veu_icon.is_hidden() == True
        assert self.Office_icon.is_hidden() == True
        assert self.Public_icon.is_hidden() == True
        assert self.Private_icon.is_hidden() == True
        assert self.Classified_icon.is_hidden() == True
        assert self.General_icon.is_hidden() == True
        assert self.Downloads_icon.is_hidden() == True
        assert self.WordFile_icon.is_hidden() == True
        assert self.ExcelFile_icon.is_hidden() == True