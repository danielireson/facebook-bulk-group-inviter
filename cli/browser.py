import os
import random
import sys
import time
import unicodedata

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class Browser:
  delay = 3

  def __init__(self):
    driver_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/phantomjs'
    self.browser = webdriver.PhantomJS(executable_path=driver_path)

  def navigate(self, url, wait_for, error):
    try:
      print('Navigating to: ' + url)
      self.browser.get(url)
      element_present = expected_conditions.presence_of_element_located((By.ID, wait_for))
      WebDriverWait(self.browser, self.delay).until(element_present)
    except TimeoutException:
      sys.exit(error)

  def enter_login_details(self, email, password):
    try:
      print('Entering login details')
      email_field = self.browser.find_element_by_id('email')
      pass_field = self.browser.find_element_by_id('pass')
      email_field.send_keys(email)
      pass_field.send_keys(password)
      pass_field.submit()
      element_present = expected_conditions.presence_of_element_located((By.ID, 'userNavigationLabel'))
      WebDriverWait(self.browser, self.delay).until(element_present)
    except TimeoutException:
      sys.exit('Login with your credentials unsuccessful')

  def import_members(self, emails):
    print('Attempting to import email addresses')
    input_xpath = "//input[@placeholder='Enter name or email address...']"
    add_members_field = self.browser.find_element_by_xpath(input_xpath)
    for email in emails:
      for c in email:
        add_members_field.send_keys(self._get_base_character(c))
      add_members_field.send_keys(Keys.RETURN)
      time.sleep(random.randint(1,self.delay))

  @staticmethod
  def _get_base_character(c):
    desc = unicodedata.name(unicode(c))
    cutoff = desc.find(' WITH ')
    if cutoff != -1:
        desc = desc[:cutoff]
    return unicodedata.lookup(desc)
