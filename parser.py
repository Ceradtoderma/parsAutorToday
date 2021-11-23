from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class ParsAT:

    def __init__(self, url, login='', password='', name='data' ):
        self.log = login
        self.password = password
        self.url = url
        self.name = name
        self.driver = webdriver.Chrome()
        self.text = ''

        self.pars = True
        self.cur_chapter = 'Начали'

    def login(self):
        self.driver.get('https://author.today/')
        log_in = self.driver.find_element(By.ID, 'navbar-right')
        log_in.click()

        sleep(1)

        self.driver.find_element(By.CLASS_NAME, 'modal-body').find_element(By.NAME, 'Login').send_keys(self.log)
        self.driver.find_element(By.CLASS_NAME, 'modal-body').find_element(By.NAME, 'Password').send_keys(self.password)
        self.driver.find_element(By.CLASS_NAME, 'modal-body').find_element(By.CLASS_NAME, 'btn-primary').click()
        sleep(2)
        self.get_text()

    def get_text(self):
        self.driver.get(self.url)
        while True:
            try:
                sleep(2)
                self.text += ' ' + self.driver.find_element(By.ID, 'text-container').text
                btn = self.driver.find_element(By.CLASS_NAME, 'next').find_element(By.TAG_NAME, 'a')
                print(btn.text)
                self.cur_chapter = btn.text
                btn.click()
            except:
                print('Страницы кончились')
                break
        self.save_text()
        self.driver.close()
        self.pars = False

    def save_text(self):
        with open(f'{self.name}.txt', 'w', encoding='utf-8') as f:
            f.write(self.text)


if __name__ == '__main__':
    pars = ParsAT('https://author.today/reader/131901/1055496', '123', 'aisavikin@gmail.com', 'eto2016Detk*')
    pars.login()
    # pars.get_text()
    print(pars.text)
#
# print(pars.text)


# def get_text(url):
#     text = ''
#
#     driver = webdriver.Chrome()
#     driver.get(url)
#     while True:
#         try:
#             text += ' ' + driver.find_element(By.ID, 'text-container').text
#             btn = driver.find_element(By.CLASS_NAME, 'next').find_element(By.TAG_NAME, 'a')
#             print(btn.text)
#             btn.click()
#             sleep(1)
#         except:
#             print('Страницы кончились')
#             break
#     return text
#
# def save_text(text, name):
#     with open(f'{name}.txt', 'w') as f:
#         f.write(text)
