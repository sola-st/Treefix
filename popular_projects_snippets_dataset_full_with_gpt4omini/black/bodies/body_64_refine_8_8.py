from typing import List, Union, Any # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error): # pragma: no cover
        self._error = error # pragma: no cover
    def err(self): # pragma: no cover
        return self._error # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
class MockToken: # pragma: no cover
    STRING = 'string' # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
class MockSelf: # pragma: no cover
    def do_match(self, line): # pragma: no cover
        return MockMatchResult() # pragma: no cover
    def do_transform(self, line, indices): # pragma: no cover
        return [MockResult()] * len(indices) # pragma: no cover
class MockMatchResult: # pragma: no cover
    def ok(self): # pragma: no cover
        return [0, 1]  # Example indices for transformation # pragma: no cover
class MockResult: # pragma: no cover
    def ok(self): # pragma: no cover
        return 'transformed line' # pragma: no cover

line = MockLine(leaves=[MockToken.STRING]) # pragma: no cover
CannotTransform = CannotTransform # pragma: no cover
self = MockSelf() # pragma: no cover
Err = Err # pragma: no cover
token = MockToken # pragma: no cover

from typing import List, Union # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error): # pragma: no cover
        self._error = error # pragma: no cover
    def err(self): # pragma: no cover
        return self._error # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
class Token: # pragma: no cover
    STRING = 'string_token_type' # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, type): # pragma: no cover
        self.type = type # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
class MockTransformer: # pragma: no cover
    def do_match(self, line): # pragma: no cover
        return MockMatchResult() # pragma: no cover
    def do_transform(self, line, indices): # pragma: no cover
        return [MockResult()] * len(indices) # pragma: no cover
class MockMatchResult: # pragma: no cover
    def ok(self): # pragma: no cover
        return [0, 1] # pragma: no cover
class MockResult: # pragma: no cover
    def ok(self): # pragma: no cover
        return 'transformed line' # pragma: no cover

line = MockLine(leaves=[Leaf(Token.STRING), Leaf('not_a_string')]) # pragma: no cover
CannotTransform = CannotTransform # pragma: no cover
self = MockTransformer() # pragma: no cover
Err = Err # pragma: no cover
token = Token # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        StringTransformer instances have a call signature that mirrors that of
        the Transformer type.

        Raises:
            CannotTransform(...) if the concrete StringTransformer class is unable
            to transform @line.
        """
# Optimization to avoid calling `self.do_match(...)` when the line does
# not contain any string.
if not any(leaf.type == token.STRING for leaf in line.leaves):
    _l_(6187)

    raise CannotTransform("There are no strings in this line.")
    _l_(6186)

match_result = self.do_match(line)
_l_(6188)

if isinstance(match_result, Err):
    _l_(6191)

    cant_transform = match_result.err()
    _l_(6189)
    raise CannotTransform(
        f"The string transformer {self.__class__.__name__} does not recognize"
        " this line as one that it can transform."
    ) from cant_transform
    _l_(6190)

string_indices = match_result.ok()
_l_(6192)

for line_result in self.do_transform(line, string_indices):
    _l_(6198)

    if isinstance(line_result, Err):
        _l_(6195)

        cant_transform = line_result.err()
        _l_(6193)
        raise CannotTransform(
            "StringTransformer failed while attempting to transform string."
        ) from cant_transform
        _l_(6194)
    line = line_result.ok()
    _l_(6196)
    aux = line
    _l_(6197)
    exit(aux)
