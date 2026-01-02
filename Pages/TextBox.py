from playwright.sync_api import Page,Expect,sync_playwright

class TextBox:
    def __init__(self,page):
        self.page = page
        self.userName_loc = self.page.locator('//input[@id="userName"]')
        self.emailAddress_loc = self.page.locator('//input[@id="userEmail"]')
        self.currentAddress_loc = self.page.locator('//textarea[@id="currentAddress"]')
        self.permAddress_loc = self.page.locator('//textarea[@id="permanentAddress"]')
        self.submit_loc =  self.page.locator('//button[@id="submit"]')
        self.verifiy_userName_loc = self.page.locator('//p[@id="name"]')
        self.verifiy_emailAddress_loc = self.page.locator('//p[@id="email"]')
        self.verifiy_CurrentAddress_loc = self.page.locator('//p[@id="currentAddress"]')
        self.verifiy_permAddress_loc = self.page.locator('//p[@id="permanentAddress"]')
    def verifiy_all_details_empty_at_first(self):
        # print(self.verifiy_userName_loc.is_visible())
        assert self.verifiy_userName_loc.is_visible() == False
        assert self.verifiy_emailAddress_loc.is_visible() == False
        assert self.verifiy_CurrentAddress_loc.is_visible() == False
        assert self.verifiy_permAddress_loc.is_visible() == False
        if self.verifiy_userName_loc.is_visible() is False and self.verifiy_emailAddress_loc.is_visible() is False and self.verifiy_CurrentAddress_loc.is_visible() is False and self.verifiy_permAddress_loc.is_visible() is False :
            return True
        else : return False
    def fill_TextBox(self,userName,emailAddress,Address,permAddress):
        self.userName_loc.clear()
        self.userName_loc.fill(userName)
        self.emailAddress_loc.clear()
        self.emailAddress_loc.fill(emailAddress)
        # print(emailAddress_loc.input_value())
        self.currentAddress_loc.clear()
        self.currentAddress_loc.fill(Address)
        self.permAddress_loc.clear()
        self.permAddress_loc.fill(permAddress)
        self.submit_loc.click()
    # def verifiyDetails(self,userName,emailAddress,Address,permAddress):
        # print(self.userName_loc.input_value().split(':'))
        # assert self.verifiy_userName_loc.inner_text().split(':')[1] == userName
        # assert self.verifiy_emailAddress_loc.inner_text().split(':')[1] == emailAddress
        # assert self.verifiy_CurrentAddress_loc.inner_text().split(':')[1] == Address
        # assert self.verifiy_permAddress_loc.inner_text().split(':')[1] == permAddress