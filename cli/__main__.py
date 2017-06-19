import argparse
import getpass

from browser import Browser
from email_loader import EmailLoader

def main():
  parser = argparse.ArgumentParser(description='This tool lets you invite people in bulk to your Facebook group')
  parser.add_argument('-e','--email', help='Your personal Facebook account email', required=True)
  parser.add_argument('-g','--group', help='The Facebook group name', required=True)
  parser.add_argument('-f','--file', help='The csv file to load email addresses from', default='emails.csv')
  args = vars(parser.parse_args())
  args['password'] = getpass.getpass()

  email_loader = EmailLoader(filename=args['file'])
  browser = Browser()
  browser.navigate(
    url='https://www.facebook.com',
    wait_for='facebook',
    error='Unable to load the Facebook website'
  )
  browser.enter_login_details(email=args['email'], password=args['password'])
  browser.navigate(
    url='https://www.facebook.com/groups/' + args['group'],
    wait_for='pagelet_group_',
    error='Couldn\'t navigate to the group\'s members page'
  )
  browser.import_members(emails=email_loader.all_emails)
  print(str(len(email_loader.all_emails)) + ' email addresses successfully imported')

if __name__ == '__main__':
  main()
