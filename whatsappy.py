from os import system as cmd
from time import sleep as wait
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
except ModuleNotFoundError:
    cmd('pip3 install selenium')
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException


class WhatsappAPI():

    @classmethod
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=%USERPROFILE%\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://web.whatsapp.com')

    @classmethod
    def send_text_message(self, contact, message):
        searchbox = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.click()
        searchbox.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        searchbox.send_keys(contact)
        con = self.driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        con.click()

        box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        box.click()
        box.send_keys(message)
        box.send_keys(Keys.ENTER)

    @classmethod
    def change_profile_name(self, name):
        menu = self.driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
        menu.click()

        wait(0.7)

        menu2 = self.driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div')
        menu2.click()

        wait(0.7)

        menu3 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]')
        menu3.click()

        wait(0.7)

        menu4 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]')
        btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[2]/div[1]/span[2]/div')
        btn.click()

        wait(0.7)

        namebox = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[2]/div[1]/div/div[2]')
        namebox.click()
        namebox.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        namebox.send_keys(name)

        confirm = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[2]/div[1]/span[2]/div')
        confirm.click()

        returning = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button')
        returning.click()
        wait(0.6)
        returning2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button')
        returning2.click()

    @classmethod
    def close(self):
        self.driver.quit()

    @classmethod
    def send_image(self, contact, path):
        searchbox = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.click()
        searchbox.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        searchbox.send_keys(contact)
        con = self.driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        con.click()

        clipbox = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div')
        clipbox.click()

        imageb = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')
        imageb.send_keys(path)

        wait(5)

        sendbt = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
        sendbt.click()

    @classmethod
    def send_document(self, contact, path):
        searchbox = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.click()
        searchbox.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        searchbox.send_keys(contact)
        con = self.driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        con.click()

        clipbox = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div')
        clipbox.click()

        docub = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[3]/button/input')
        docub.send_keys(path)

        wait(5)

        sendbt = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
        sendbt.click()

    @classmethod
    def take_shot(self, contact):
        searchbox = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.click()
        searchbox.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        searchbox.send_keys(contact)
        con = self.driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        con.click()

        clipbox = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        clipbox.click()

        wait(0.6)

        cambox = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[2]/button/span')
        cambox.click()

        wait(1)

        cambtn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div')
        cambtn.click()

        wait(1)

        sendbtn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
        sendbtn.click()

    @classmethod
    def send_contact(self, contact, sendthiscontact):
        searchbox = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.click()
        searchbox.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        searchbox.send_keys(contact)
        con = self.driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        con.click()

        wait(0.4)

        clipbox = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div')
        clipbox.click()

        wait(0.4)

        contactbox = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[4]/button/span')
        contactbox.click()

        wait(0.4)

        search = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/label/div/div[2]')
        search.click()
        search.send_keys(sendthiscontact)

        wait(0.4)

        finalcontact = self.driver.find_element_by_xpath(f'//*[@title="{sendthiscontact}"]')
        finalcontact.click()

        wait(0.4)

        sendbtn = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span/div/div/div')
        sendbtn.click()

        wait(0.4)

        sendbtn2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div')
        sendbtn2.click()

    @classmethod
    def block_contact(self, contact):
        searchbox = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.click()
        searchbox.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        searchbox.send_keys(contact)
        con = self.driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        con.click()

        info = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
        info.click()

        blok = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[6]/div/div[2]')
        blok.click()

        confirmblok = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
        confirmblok.click()

    @classmethod
    def unblock_contact(self, contact):
        searchbox = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.click()
        searchbox.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        searchbox.send_keys(contact)
        con = self.driver.find_element_by_xpath(f'//*[@title="{contact}"]')
        con.click()

        info = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
        info.click()

        wait(0.6)

        unblok = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[6]/div/div[2]')
        unblok.click()

        wait(0.6)

        confirmunblok = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
        confirmunblok.click()

    @classmethod
    def change_theme(self, theme):
        menu = self.driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
        menu.click()

        wait(0.7)

        menu2 = self.driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div')
        menu2.click()

        wait(0.7)

        menu3 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[3]/div[2]')
        menu3.click()

        wait(0.7)

        if theme.lower() == 'black' or 'gray':
            menu4 = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[2]/label/input')
            wait(0.7)
            menu4.click()
            btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div[2]')
            btn.click()

        if theme.lower() == 'white':
            menu4 = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[1]/label/input')
            wait(0.7)
            menu4.click()
            btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div[2]')
            btn.click()

    @classmethod
    def change_profile_picture(self, path):
        profile = self.driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
        profile.click()

        profilech = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/input')
        profilech.send_keys(path)

        wait(10)

        btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div')
        btn.click()

        returning = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/header/div/div[1]/button/span')
        returning.click()

    @classmethod
    def change_profile_description(self, description):
        profile = self.driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
        profile.click()

        wait(0.6)

        edit = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/span[2]/div')
        edit.click()

        wait(0.6)

        text = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/div/div[2]')
        text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        text.send_keys(description)
        text.send_keys(Keys.ENTER)

        returning = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/header/div/div[1]/button/span')
        returning.click()

    @classmethod
    def create_group(self, contacts, groupname, path):
        gr = self.driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div')
        gr.click()

        wait(0.5)

        gr2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div[1]/div[2]')
        gr2.click()

        typ = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input')
        typ.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

        wait(0.5)

        for people in contacts:

            typ.click()

            wait(0.5)

            wait(0.5)

            typ.send_keys(people)

            contacc = self.driver.find_element_by_xpath(f'//*[@title="{people}"]')

            wait(0.5)

            contacc.click()

        btn1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div')
        btn1.click()

        sendimg = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/input')
        sendimg.send_keys(path)

        snibtn = self.driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div')
        snibtn.click()

        grname = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]')
        grname.click()
        grname.send_keys(groupname)

        create = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div')
        create.click()

    @classmethod
    def wait_page(self):
        delay = 60 # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[1]/div')))
            print ("Page is ready!")
            wait(0.6)
        except TimeoutException:
            print ("Error")
