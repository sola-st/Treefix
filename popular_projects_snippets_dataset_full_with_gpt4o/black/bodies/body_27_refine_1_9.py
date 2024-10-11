from typing import List # pragma: no cover
import random # pragma: no cover

class MockMode: # pragma: no cover
    def __init__(self, line_length: int): # pragma: no cover
        self.line_length = line_length # pragma: no cover
 # pragma: no cover
def generate_trailers_to_omit(line: str, line_length: int) -> List[int]: # pragma: no cover
    return [random.randint(0, line_length) for _ in range(5)] # pragma: no cover
 # pragma: no cover
line = 'sample line content' # pragma: no cover
 # pragma: no cover
mode = MockMode(line_length=80) # pragma: no cover
 # pragma: no cover
def right_hand_split(line: str, line_length: int, features: List[str], omit: int = 0) -> List[str]: # pragma: no cover
    return ['splitted line part 1', 'splitted line part 2'] # pragma: no cover
 # pragma: no cover
features = ['feature1', 'feature2'] # pragma: no cover
 # pragma: no cover
def is_line_short_enough(line: str, line_length: int) -> bool: # pragma: no cover
    return len(line) <= line_length # pragma: no cover

from typing import List # pragma: no cover

class MockMode: # pragma: no cover
    def __init__(self, line_length: int): # pragma: no cover
        self.line_length = line_length # pragma: no cover
 # pragma: no cover
def generate_trailers_to_omit(line: str, line_length: int) -> List[int]: # pragma: no cover
    return [0, 2, 4] # pragma: no cover
 # pragma: no cover
line = 'sample line content that is sufficiently long for the purpose of testing right-hand splitting and ensuring there are multiple parts to split.' # pragma: no cover
 # pragma: no cover
mode = MockMode(line_length=80) # pragma: no cover
 # pragma: no cover
def right_hand_split(line: str, line_length: int, features: List[str], omit: int = 0) -> List[str]: # pragma: no cover
    split_point = min(len(line), line_length) # pragma: no cover
    return [line[:split_point], line[split_point:]] if split_point < len(line) else [line] # pragma: no cover
 # pragma: no cover
features = ['feature1', 'feature2'] # pragma: no cover
 # pragma: no cover
def is_line_short_enough(line: str, line_length: int) -> bool: # pragma: no cover
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
