import json, xlrd
import datetime as dt

# This is the Excel data (no keys)
filename = 'people_from_excel.json'

# Open the file(standard file open stuff)
with open(filename, 'r', encoding = 'utf-8', newline = '') as f:
    # Load the whole json file into an object named people
    people = json.load(f)

# Dictionaries are in a list, loop through and display each dictionary
for p in people:
    name = p['Full Name']
    byear = p['Birth Year']
    # Excel date pretty tricky use xlrd module.
    y, m, d, h, i, s = xlrd.xldate_as_tuple(p['Date Joined'], 0)
    joined = dt.date(y, m, d)
    balance = '$' + f"{p['Balance']:,.2f}"
    print(f"{name:<22} {byear} {joined:%m/%d/%Y} {balance:>12}")