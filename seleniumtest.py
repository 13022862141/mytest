from selenium import webdriver
import time

test1 = webdriver.Firefox()

time.sleep(5)

test1.get('http://localhost:8000')

time.sleep(5)

assert 'django' in test1.title
