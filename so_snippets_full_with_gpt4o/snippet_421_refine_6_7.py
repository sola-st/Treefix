import operator # pragma: no cover

some_function = operator.sub # pragma: no cover

def some_function(input_str): # pragma: no cover
    # Convert string components to integers before performing arithmetic operations # pragma: no cover
    num_list = list(map(int, input_str.split('+'))) # pragma: no cover
    return sum(num_list) - 4 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4172448/is-it-possible-to-break-a-long-line-to-multiple-lines-in-python
from l3.Runtime import _l_
a = some_function(
    '1' + '2' + '3' - '4')
_l_(13265)

a = '1'   \
    + '2' \
    + '3' \
    - '4'
_l_(13266)

