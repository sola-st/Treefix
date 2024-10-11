import random # pragma: no cover

def generate_trailers_to_omit(line, line_length):# pragma: no cover
    return [random.randint(0, min(len(line) // 2, 10)) for _ in range(3)] # pragma: no cover
line = 'example_line_that_is_long_enough_to_be_split' # pragma: no cover
mode = type('Mock', (object,), {'line_length': 40}) # pragma: no cover
def right_hand_split(line, line_length, features, omit=0):# pragma: no cover
    splits = [line[i:i+line_length] for i in range(0, len(line), line_length)]# pragma: no cover
    if omit > 0 and len(splits) > omit:# pragma: no cover
        splits = splits[:-omit]# pragma: no cover
    return splits # pragma: no cover
features = {'dummy_feature': True} # pragma: no cover
def is_line_short_enough(line, line_length):# pragma: no cover
    return len(line) <= line_length # pragma: no cover

from typing import List, Generator # pragma: no cover

def generate_trailers_to_omit(line: str, line_length: int) -> Generator[int, None, None]:# pragma: no cover
    # Mock generator function# pragma: no cover
    yield 0# pragma: no cover
    yield 1# pragma: no cover
    yield 2 # pragma: no cover
line = 'example_line_that_is_long_enough_to_be_split' # pragma: no cover
class Mode:# pragma: no cover
    def __init__(self, line_length: int):# pragma: no cover
        self.line_length = line_length# pragma: no cover
mode = Mode(line_length=40) # pragma: no cover
def right_hand_split(line: str, line_length: int, features: List[str], omit: int) -> List[str]:# pragma: no cover
    # Mock splitting function# pragma: no cover
    if omit == 0:# pragma: no cover
        return [line[:line_length], line[line_length:]]# pragma: no cover
    return [line[:line_length - omit], line[line_length - omit:]] # pragma: no cover
features = ['dummy_feature1', 'dummy_feature2'] # pragma: no cover
def is_line_short_enough(line: str, line_length: int) -> bool:# pragma: no cover
    # Mock check function# pragma: no cover
    return len(line) <= line_length # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Wraps calls to `right_hand_split`.

            The calls increasingly `omit` right-hand trailers (bracket pairs with
            content), meaning the trailers get glued together to split on another
            bracket pair instead.
            """
for omit in generate_trailers_to_omit(line, mode.line_length):
    _l_(16303)

    lines = list(
        right_hand_split(line, mode.line_length, features, omit=omit)
    )
    _l_(16299)
    # Note: this check is only able to figure out if the first line of the
    # *current* transformation fits in the line length.  This is true only
    # for simple cases.  All others require running more transforms via
    # `transform_line()`.  This check doesn't know if those would succeed.
    if is_line_short_enough(lines[0], line_length=mode.line_length):
        _l_(16302)

        aux = lines
        _l_(16300)
        exit(aux)
        exit()
        _l_(16301)
aux = right_hand_split(
    line, line_length=mode.line_length, features=features
)
_l_(16304)
exit(aux)
