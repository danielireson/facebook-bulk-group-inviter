import argparse
import csv
import os
import sys
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

parser = argparse.ArgumentParser(description='This tool lets you invite people in bulk to your Facebook group')
parser.add_argument('-e','--email', help='Your personal Facebook account email', required=True)
parser.add_argument('-p','--password', help='Your password in plain text', required=True)
parser.add_argument('-g','--group', help='The Facebook group name', required=True)
parser.add_argument('-f','--file', help='The csv file to load email addresses from', default='emails.csv')
args = vars(parser.parse_args())

if not os.path.isfile(args['file']):
  sys.exit('File does not exist: ' + args['file'])

# Load the Facebook login page
delay = 3
browser = webdriver.Firefox(executable_path=os.getcwd() + '/geckodriver')
browser.get('https://www.facebook.com')

# Enter email and password at the login page
email_field = browser.find_element_by_id('email')
pass_field = browser.find_element_by_id('pass')
email_field.send_keys(args['email'])
pass_field.send_keys(args['password'])
pass_field.submit()

# Ensure the login was successful
try:
  element_present = expected_conditions.presence_of_element_located((By.ID, 'userNavigationLabel'))
  WebDriverWait(browser, delay).until(element_present)
except TimeoutException:
  sys.exit('Unable to login, check your credentials')

# Load the group's page
try:
  element_present = expected_conditions.presence_of_element_located((By.ID, 'pagelet_group_'))
  browser.get('https://www.facebook.com/groups/' + args['group'])
  WebDriverWait(browser, delay).until(element_present)
except TimeoutException:
  sys.exit('Couldn\'t navigate to the group\'s members page')

# Load emails into memory
emails = []
with open(args['file'], 'rb') as file:
  csv_reader = csv.reader(file)
  for email in csv_reader:
    emails.append(email[0])
