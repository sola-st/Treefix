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
    # Simulating omits for example purpose # pragma: no cover
    return [i for i in range(min(5, len(line)))] # pragma: no cover
 # pragma: no cover
line = "sample line content right here" # pragma: no cover
 # pragma: no cover
mode = MockMode(line_length=30) # pragma: no cover
 # pragma: no cover
def right_hand_split(line: str, line_length: int, features: List[str], omit: int = 0) -> List[str]: # pragma: no cover
    # Ensure the line splits properly for a non-trivial case # pragma: no cover
    parts = [line[i:i + line_length] for i in range(0, len(line), line_length) if i >= omit] # pragma: no cover
    return parts if parts else [line] # pragma: no cover
 # pragma: no cover
features = ["feature1", "feature2"] # pragma: no cover
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
