from selenium import webdriver
import time

btn_ele = r'#su'
url = r"https://www.baidu.com/"


def vote(url, btn):
    global browser
    browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    browser.get(url)
    while True:
        loop(btn, browser)
        time.sleep(1)
        browser.refresh()
        time.sleep(2)


def loop(btn, browser):
    for i in range(1, 15):
        browser.find_element_by_css_selector(btn).click()


vote(url, btn_ele)
