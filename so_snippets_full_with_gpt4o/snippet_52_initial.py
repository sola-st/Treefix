# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
from l3.Runtime import _l_
py = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
_l_(12200)

sort_on = "name"
_l_(12201)
decorated = [(dict_[sort_on], dict_) for dict_ in py]
_l_(12202)
decorated.sort()
_l_(12203)
result = [dict_ for (key, dict_) in decorated]
_l_(12204)

result
_l_(12205)
[{'age': 10, 'name': 'Bart'}, {'age': 39, 'name': 'Homer'}]
_l_(12206)

