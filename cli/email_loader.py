import csv
import os
import sys

class EmailLoader:
  all_emails = []

  def __init__(self, filename):
    file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/' + filename
    if not os.path.isfile(file_path):
      sys.exit('File does not exist: ' + filename)

    with open(file_path, 'rb') as file:
      csv_reader = csv.reader(file)
      for email in csv_reader:
        self.all_emails.append(email[0])

    if len(self.all_emails) < 1:
      sys.exit('There are no emails in your supplied file')
    else:
      print('Loaded ' + str(len(self.all_emails)) + ' emails from ' + filename)
