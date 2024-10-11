import string # pragma: no cover

string = 'Sample string with spaces for testing\\\\ escape sequences.' # pragma: no cover
i = 13 # pragma: no cover
def is_valid_index(index): return 0 <= index < len(string) # pragma: no cover
self = type('Mock', (object,), {'MIN_SUBSTR_SIZE': 5})() # pragma: no cover
def breaks_unsplittable_expression(index): return False # pragma: no cover

 # pragma: no cover

string = 'Sample string with spaces for testing\\ escape sequences.' # pragma: no cover
i = 13 # pragma: no cover
def is_valid_index(index): return 0 <= index < len(string) # pragma: no cover
self = type('Mock', (object,), {'MIN_SUBSTR_SIZE': 5})() # pragma: no cover
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
_l_(17215)

is_not_escaped = True
_l_(17216)
j = i - 1
_l_(17217)
while is_valid_index(j) and string[j] == "\\":
    _l_(17220)

    is_not_escaped = not is_not_escaped
    _l_(17218)
    j -= 1
    _l_(17219)

is_big_enough = (
    len(string[i:]) >= self.MIN_SUBSTR_SIZE
    and len(string[:i]) >= self.MIN_SUBSTR_SIZE
)
_l_(17221)
aux = (
    is_space
    and is_not_escaped
    and is_big_enough
    and not breaks_unsplittable_expression(i)
)
_l_(17222)
exit(aux)
