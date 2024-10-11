# Extracted from https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
names = ['bob', 'john', 'mike']
any(st in 'bob and john' for st in names) 
>> True

any(st in 'mary and jane' for st in names) 
>> False

