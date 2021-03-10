# Open the file with encoding set to utf-8.
with open('names.txt', 'r', encoding = 'utf-8') as f:
    # Read entire file into variable named content
    content = f.read()
    # Show that content.
    print(content) 