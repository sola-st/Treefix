i = 3 # pragma: no cover
string = 'abc ' # pragma: no cover
self = type('Mock', (object,), {'MIN_SUBSTR_SIZE': 2})() # pragma: no cover
def is_valid_index(index): return 0 <= index < len(string) # pragma: no cover
def breaks_unsplittable_expression(index): return False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
            Returns:
                True iff ALL of the conditions listed in the 'Transformations'
                section of this classes' docstring would be be met by returning @i.
            """
is_space = string[i] == " "
_l_(5794)

is_not_escaped = True
_l_(5795)
j = i - 1
_l_(5796)
while is_valid_index(j) and string[j] == "\\":
    _l_(5799)

    is_not_escaped = not is_not_escaped
    _l_(5797)
    j -= 1
    _l_(5798)

is_big_enough = (
    len(string[i:]) >= self.MIN_SUBSTR_SIZE
    and len(string[:i]) >= self.MIN_SUBSTR_SIZE
)
_l_(5800)
aux = (
    is_space
    and is_not_escaped
    and is_big_enough
    and not breaks_unsplittable_expression(i)
)
_l_(5801)
exit(aux)
