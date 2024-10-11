# Extracted from https://stackoverflow.com/questions/4978738/is-there-a-python-equivalent-of-the-c-sharp-null-coalescing-operator
Python has a get function that its very useful to return a value of an existent key, if the key exist;
if not it will return a default value.

def main():
    names = ['Jack','Maria','Betsy','James','Jack']
    names_repeated = dict()
    default_value = 0

    for find_name in names:
        names_repeated[find_name] = names_repeated.get(find_name, default_value) + 1

