# Bulk email inviter for Facebook groups
This is a quick tool that allows you to invite members to your Facebook group via email in bulk. I put it together for use at the Manchester Entrepreneurs society at the start of the year to import our new fresher's member list to our active Facebook group.

## How it works
It was built in Python (2.7) and uses selenium/webdriver. The Mozilla geckodriver has been included in the repository but please ensure you have the latest version of firefox installed or it will not work.

## Installing
``` bash
# from the facebook-bulk-group-inviter directory
pip install .

# install with editable flag if you plan on making changes
pip install -e .
```

## Getting started
Invoke *facebook-bulk-group-inviter* from the command line with arguments *-e*, *-p* and *-g* with your facebook email, password and group name (or number) respectively. 

``` bash
# run the import
facebook-bulk-group-inviter -e email@example.com -p password -g nameornumber
```

By default email addresses will be loaded from *emails.csv* in the package directory but you can override this by passing a new file name with the *-f* parameter. Emails should be on a new line and in the first column. There can be other columns in the csv file but the email address has to be in the first column. Please also ensure your csv has no headers.

