from selenium import webdriver

browser = webdriver.Chrome('/Users/ardila/src/tdd_tutorial/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
