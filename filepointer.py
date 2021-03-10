# Using tell() to determine pointer location
with open('names.txt', encoding = 'utf-8') as f:
    # Read the first line to get started
    print(f.tell())
    one_line = f.readline()
    while one_line:
        print(one_line[:-1], f.tell())
        one_line = f.readline()
