from playwright.sync_api import Page,Expect,sync_playwright


class practiceForm:
    def __init__(self,page):
        self.page = page
        self.FirstName_loc = self.page.locator("//input[@id='firstName']")
        self.LastName_loc = self.page.locator("//input[@id='lastName']")
        self.userEmail_loc = self.page.locator("//input[@id='userEmail']")
        self.gender_male_loc = self.page.locator("//input[@name='gender' and @value='Male']")
        self.gender_female_loc = self.page.locator("//input[@name='gender' and @value='Female']")
        self.gender_other_loc = self.page.locator("//input[@name='gender' and @value='Other']")
        self.mobNumber_loc = self.page.locator("//input[@id='userNumber']")
        self.dateOfBirth_input_loc = self.page.locator("//input[@id='dateOfBirthInput']")
        self.Month_input_loc = self.page.locator("//select[@class='react-datepicker__month-select']")
        self.Year_input_loc = self.page.locator("//select[@class='react-datepicker__year-select']")
        self.date_input_loc = self.page.locator("div").filter(has_text="5").first
        self.subjects_loc = self.page.locator("//input[@id='subjectsInput']")
        self.Hobbies_sports_loc =self.page.get_by_label("Sports", exact=True)
        self.Hobbies_Reading_loc = self.page.get_by_label("Reading", exact=True)
        self.Hobbies_Music_loc = self.page.get_by_label("Music", exact=True)
        self.UploadPic_loc = self.page.locator("//input[@id='uploadPicture']")
        self.currentAddress_loc = self.page.locator("//textarea[@id='currentAddress']")
        self.StateSel_loc = self.page.locator("(//input[@id='react-select-3-input'])[1]")
        self.CitySel_loc = self.page.locator("(//input[@id='react-select-4-input'])[1]")
        self.submit_loc = self.page.locator("//button[@id='submit']")
    def fillfirstName(self,firstName):
        self.FirstName_loc.clear()
        self.FirstName_loc.fill(firstName)
    def filllastName(self,lastName):
        self.LastName_loc.clear()
        self.LastName_loc.fill(lastName)
    def filluserEmail(self,useremail):
        self.userEmail_loc.clear()
        self.userEmail_loc.fill(useremail)
    def fillGender(self,gender):
        if gender == 'male' :
            self.gender_male_loc.click(force = True)
        elif gender == 'female':
            self.gender_female_loc.click(force = True)
        else :
            self.gender_other_loc.first.click(force = True)
    def fillMobileNumber(self,mobNumber):
        self.mobNumber_loc.clear()
        self.mobNumber_loc.fill(mobNumber)
    def fillHobbies(self,Hobby):
        if str(Hobby).lower() == 'sports' :
            self.Hobbies_sports_loc.click(force = True)
        elif str(Hobby).lower() == 'music':
            self.Hobbies_Music_loc.click(force = True)
        elif str(Hobby).lower() == 'reading' :
            self.Hobbies_Reading_loc.click(force = True)
        elif str(Hobby).lower() == 'all':
            self.Hobbies_Music_loc.click(force = True)
            self.Hobbies_Reading_loc.click(force = True)
            self.Hobbies_sports_loc.click(force = True)
    def uploadPic(self,picurl) :
        self.UploadPic_loc.clear()
        self.UploadPic_loc.fill(picurl)
    def fillcurrentAddress(self,Address):
        self.currentAddress_loc.clear()
        self.currentAddress_loc.fill(Address)
    def selectState(self,state):
        self.StateSel_loc.fill(state)
        self.page.keyboard.press('Tab')
    def selectcity(self,city):
        self.CitySel_loc.fill(city)
        self.page.keyboard.press('Tab')
    def submitForm(self):
        self.submit_loc.click()
    def datePicker(self):
        self.dateOfBirth_input_loc.click()
        # self.page.wait_for_selector(self.Month_input_loc,state='visible')
        self.Month_input_loc.select_option('June')
        self.Year_input_loc.select_option('1992')
        self.page.wait_for_timeout(2000)
        self.date_input_loc.click(force = True)
    def inputSubject(self,subjectName) :
        self.subjects_loc.fill(subjectName)
        self.page.keyboard.press('Tab')




        