from selenium import webdriver
import time

vote_btn = r'body > div.container > div:nth-child(2) > div.smallVideo-container > ul > li:nth-child(5) > div > div.smallVideo-voteBtn-div'
vote_url = r"http://tech.sina.cn/event/sina20/?from=groupmessage"
cookie_url = r'chrome://settings/clearBrowserData'
cookie_btn = r'#clearBrowsingDataConfirm'


def vote(url, btn):
    global browser
    browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    while True:
        loop(btn, url, browser)
        time.sleep(1)
        clear_cookies(cookie_btn, cookie_url, browser)
        time.sleep(1)


def loop(btn, url, browser):
    browser.get(url)
    time.sleep(2)
    for i in range(1, 15):
        browser.find_element_by_css_selector(btn).click()


def clear_cookies(btn, url, browser):
    # browser.get(url)
    # time.sleep(5)
    # browser.find_element_by_css_selector(btn).click()
    browser.delete_all_cookies()


vote(vote_url, vote_btn)
