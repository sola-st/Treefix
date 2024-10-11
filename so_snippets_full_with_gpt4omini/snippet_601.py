# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1373164/how-do-i-create-variable-variables
# using dictionary
from l3.Runtime import _l_
variables = {}
_l_(2674)
variables["first"] = 34
_l_(2675)
variables["second"] = 45
_l_(2676)
print(variables["first"], variables["second"])
_l_(2677)

# using namedtuple
Variables = namedtuple('Variables', ['first', 'second'])
_l_(2678)
vars = Variables(34, 45)
_l_(2679)
print(vars.first, vars.second)
_l_(2680)

