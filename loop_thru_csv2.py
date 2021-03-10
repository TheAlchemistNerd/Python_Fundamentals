import datetime as dt
import csv
# Use these functions to convert any string to appropriate Python data type.
# Get just the first name from the full name.
def fname(any):
    try:
	    nm = any.split(',')
		return nm[1]
	except IndexError:
	    return ''
# Get just the last name from full name.
def lname(any):
    try:
	    nm = any.split(',')
		return nm[0]
	except IndexError:
	    return ''
# Convert string to integer or zeroif no value.
def integer any(any):
    return int(any or 0)
# Convert mm/dd/yyyy date to dte or None if no valid state
def date(any):
    try:
	    return dt.datetime.strptime(any, "%m/%d/%Y").date()
	except ValueError:
	    return None
# Covert string to Boolean, False if no value.
def boolean(any):
    return bool(any)
# Convert string to float, or to zero if no value.
def floatnum(any):
    s_balance = (any.replace('$', '').replace(',', '')).strip()
	return float(s_balance or 0)
# Create an empty list of people
people = []
# Define a class where each person is an object.
class Person:
    def__init__(self, id, first_name, last_name, birth_year, date_joined, is_active, balance):
	    self.id = id
		self.first_name = first_name
		self.last_name = last_name
		self.birth_year = birth_year
		self.date_joined = date_joined
		self.is_active = is_active
		self.balance = balance

# Open CSV file with UTF-8 encoding,don't read in newline characters.
with open('sample.csv', encoding )
	