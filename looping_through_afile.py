# looping with readlines()
with open('quotes.txt') as f:
    # Read in all lies first, then loops through.
    for one_line in f.readlines():
        print(one_line, end = '')  # the "end = '' " helps retain single spacing
print()


# this code indents the name by a space putting an extra
# blank line beneath it
with open('quotes.txt') as f:
    # Reads in all lines first, then loops through.
    # Count ea line starting at zero
    for one_line in enumerate(f.readlines()):
        if one_line[0] % 2 == 0:
            print(one_line[1], end = '')
            # Otherwise print a couple spaces and an extra newline.
        else:
            print('    ' + one_line[1])
print()


# looping with readline()
with open('quotes.txt') as f:
    one_line = f.readline()
    while one_line:
        print(one_line, end = '')
        one_line = f.readline()
print()


""" this code indents the name by a space putting an extra
    blank line beneath it
"""
# store a number to use as a loop counter
counter = 1
# oen the file
with open('quotes.txt') as f:
    # Rea one line from the file
    one_line = f.readline()
    # As long  there a lines to read ...
    while one_line:
        # If the counter is an even number, print a couple spaces.
        if counter % 2 == 0:
            print('    ' + one_line)
        # Otherwise print with no newline at the end.
        else:
            print(one_line, end = '')
        # Increment the counter
        counter += 1
        # Read the next line.
        one_line = f.readline() 
