# Basic syntax to open, read and display file contents
f = open('quotes.txt')
filecontents = f.read()
print(filecontents)
# Returns True if the file is closed, otherwise false.
print('File is closed: ', f.closed)

# Closes the file.
f.close() # Print a blank line

# ------------------ Contextual syntax
with open('quotes.txt') as f:
    filecontents = f.read()
    print(filecontents)

# the unindented line below is outside the with... block;
print('File is closed: ', f.closed)
