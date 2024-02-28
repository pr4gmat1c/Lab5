def replace(str):
    to_replace = [' ', ',', '.']
    for x in to_replace:
        str = str.replace(x, ':')
    return str


str = input("Enter text:")
replaced_string = replace(str)
print("New text:", replaced_string)
