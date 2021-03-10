# New name to add with \n to mark end of line.
new_name = 'Peña Calderón\n'
# Open names.txt in append mode with encoding.
with open('names.txt', 'a', encoding = 'utf-8') as f:
    # add the new name and \n to the end of the file.
    f.write(new_name)

# File closes automatically after indentions
print('\nDone')
# Re-open te file with encoding and display the contents
with open('names.txt', encoding = 'utf-8') as f:
    print(f.read())