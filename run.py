#!/usr/bin/env python

import argparse
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

parser = argparse.ArgumentParser(description='This tool lets you invite people in bulk to your Facebook group')
parser.add_argument('-e','--email', help='Your personal Facebook account email', required=True)
parser.add_argument('-p','--password', help='Your password in plain text', required=True)
parser.add_argument('-f','--file', help='The csv file to load email addresses from', default='emails.csv')
args = vars(parser.parse_args())

delay = 3
browser = webdriver.Firefox(executable_path=os.getcwd() + '/geckodriver')
browser.get('https://www.facebook.com')

email_field = browser.find_element_by_id('email')
pass_field = browser.find_element_by_id('pass')
email_field.send_keys(args['email'])
pass_field.send_keys(args['password'])
pass_field.submit()

try:
  # Ensure the login was successful
  element_present = expected_conditions.presence_of_element_located((By.ID, 'userNavigationLabel'))
  WebDriverWait(browser, delay).until(element_present)
except TimeoutException:
  print 'Logging in took too long'

browser.close()
