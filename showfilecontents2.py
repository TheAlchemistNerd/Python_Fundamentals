# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

# Your custom error (inherits from Error)
class EmptyFileError(Error):
    pass

try:
    # Open the file (no error check for this example).
    thefile = open('people.csv')
    # Count the number of lines in file.
    line_count = len(thefile.readlines())
    # If there is fewer than 2 lines, raise exception.
    if line_count < 2:
        raise EmptyFileError

# Handles missing file error.
except FileNotFoundError:
        print('\nThere is no people2.csv file here')

# handles my custom error for too few rows.
except EmptyFileError:
        print("\nYour people.csv file doesn't have enough stuff.")
        
# Handles all other exceptions
except Exception as e:
        # Show the error.
        print('\n\nFailed: The error was ' + str(e))
        # Close the file.
        thefile.close()
else:
    # this code runs only if no exceptions above.
    print() # Print a blank line
    
    # File must be open by now if we got here, show contents.
    for one_line in thefile:
        print(one_line)
    thefile.close()
    print("Success!")