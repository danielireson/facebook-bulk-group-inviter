#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='This tool lets you invite people in bulk to your Facebook group')
parser.add_argument('-e','--email', help='Your personal Facebook account email', required=True)
parser.add_argument('-p','--password', help='Your password in plain text', required=True)
parser.add_argument('-f','--file', help='The csv file to load email addresses from', default='emails.csv')
args = vars(parser.parse_args())
