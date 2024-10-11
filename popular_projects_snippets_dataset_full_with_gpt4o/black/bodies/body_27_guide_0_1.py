import random # pragma: no cover

line = 'sample line with some balanced (brackets) to test the code' # pragma: no cover
mode = type('Mode', (object,), {'line_length': 80}) # pragma: no cover
features = ['F1', 'F2', 'F3'] # pragma: no cover
def generate_trailers_to_omit(line, line_length): # pragma: no cover
    # Generates a list of trailers to omit as an example # pragma: no cover
    return [[], ['F1'], ['F1', 'F2']] # pragma: no cover
def right_hand_split(line, line_length, features, omit): # pragma: no cover
    # Example split function that pretends to split by right hand brackets # pragma: no cover
    return [line[:line_length//2], line[line_length//2:]] # pragma: no cover
def is_line_short_enough(line, line_length): # pragma: no cover
    # Checks if the line length is short enough # pragma: no cover
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
