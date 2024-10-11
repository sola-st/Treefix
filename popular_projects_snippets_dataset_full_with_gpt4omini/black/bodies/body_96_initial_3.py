from typing import List # pragma: no cover
from typing import Callable # pragma: no cover

string = 'example string with escape \ character' # pragma: no cover
i = 5 # pragma: no cover
def is_valid_index(index: int) -> bool:# pragma: no cover
    return 0 <= index < len(string) # pragma: no cover
class Mock:# pragma: no cover
    MIN_SUBSTR_SIZE = 3# pragma: no cover
    def breaks_unsplittable_expression(self, index: int) -> bool:# pragma: no cover
        return False# pragma: no cover
self = Mock() # pragma: no cover

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
