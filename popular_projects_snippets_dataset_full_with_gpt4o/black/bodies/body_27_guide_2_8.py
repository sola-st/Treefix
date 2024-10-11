import sys # pragma: no cover

line = 'This is a sample line with (content) [and more content].' # pragma: no cover
mode = type('MockMode', (object,), {'line_length': 30})() # pragma: no cover
features = [] # pragma: no cover
def generate_trailers_to_omit(line, line_length): # pragma: no cover
    yield None # pragma: no cover
    yield ['[and more content]'] # pragma: no cover
def right_hand_split(line, line_length, features, omit=None): # pragma: no cover
    if omit == ['[and more content]']: # pragma: no cover
        split_point = line.index('[') # pragma: no cover
        return [line[:split_point], line[split_point:]] # pragma: no cover
    return [line] # pragma: no cover
def is_line_short_enough(line, line_length): # pragma: no cover
    return len(line) <= line_length # pragma: no cover
exit = sys.exit # pragma: no cover

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
