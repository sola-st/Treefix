from typing import List, Any # pragma: no cover
from random import choice # pragma: no cover

def right_hand_split(line: str, line_length: int, features: Any, omit: Any) -> List[str]: # pragma: no cover
    return [line] if len(line) <= line_length else [line[:line_length], line[line_length:]] # pragma: no cover
 # pragma: no cover
def is_line_short_enough(line: List[str], line_length: int) -> bool: # pragma: no cover
    return sum(len(l) for l in line) <= line_length # pragma: no cover
 # pragma: no cover
class Mode: # pragma: no cover
    def __init__(self, line_length: int): # pragma: no cover
        self.line_length = line_length # pragma: no cover
 # pragma: no cover
def generate_trailers_to_omit(line: str, line_length: int) -> List[Any]: # pragma: no cover
    return [choice([None, 'trailer1', 'trailer2']) for _ in range(3)] # pragma: no cover
 # pragma: no cover
line = 'This is a sample line that is quite long and might need splitting.' # pragma: no cover
mode = Mode(line_length=20) # pragma: no cover
features = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Wraps calls to `right_hand_split`.

            The calls increasingly `omit` right-hand trailers (bracket pairs with
            content), meaning the trailers get glued together to split on another
            bracket pair instead.
            """
for omit in generate_trailers_to_omit(line, mode.line_length):
    _l_(4518)

    lines = list(
        right_hand_split(line, mode.line_length, features, omit=omit)
    )
    _l_(4514)
    # Note: this check is only able to figure out if the first line of the
    # *current* transformation fits in the line length.  This is true only
    # for simple cases.  All others require running more transforms via
    # `transform_line()`.  This check doesn't know if those would succeed.
    if is_line_short_enough(lines[0], line_length=mode.line_length):
        _l_(4517)

        aux = lines
        _l_(4515)
        exit(aux)
        exit()
        _l_(4516)
aux = right_hand_split(
    line, line_length=mode.line_length, features=features
)
_l_(4519)
exit(aux)
