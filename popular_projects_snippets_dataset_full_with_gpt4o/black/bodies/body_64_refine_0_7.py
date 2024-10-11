from dataclasses import dataclass # pragma: no cover
from typing import Any, List # pragma: no cover

@dataclass # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Any] # pragma: no cover
line = Line(leaves=[type('Mock', (object,), {'type': 'STRING'})()]) # pragma: no cover
 # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
Err = type('Err', (object,), {'err': lambda self: CannotTransform('error')}) # pragma: no cover
 # pragma: no cover
token = type('MockToken', (object,), {'STRING': 'STRING'}) # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'do_match': lambda self, line: type('MatchResult', (object,), { # pragma: no cover
        'ok': lambda: [1, 2, 3], # pragma: no cover
        'err': lambda: None # pragma: no cover
    })(), # pragma: no cover
    'do_transform': lambda self, line, indices: [type('TransformResult', (object,), { # pragma: no cover
        'ok': lambda: 'transformed_line', # pragma: no cover
        'err': lambda: None # pragma: no cover
    })()] # pragma: no cover
})() # pragma: no cover

from dataclasses import dataclass # pragma: no cover
from typing import Any, List, Union # pragma: no cover

@dataclass # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Any] # pragma: no cover
line = Line(leaves=[type('Mock', (object,), {'type': 'STRING'})()]) # pragma: no cover
 # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, message): # pragma: no cover
        self._message = message # pragma: no cover
    def err(self): # pragma: no cover
        return CannotTransform(self._message) # pragma: no cover
 # pragma: no cover
token = type('MockToken', (object,), {'STRING': 'STRING'}) # pragma: no cover
 # pragma: no cover
class MatchResult: # pragma: no cover
    def ok(self): # pragma: no cover
        return [1, 2, 3] # pragma: no cover
    def err(self): # pragma: no cover
        return None # pragma: no cover
 # pragma: no cover
class TransformResult: # pragma: no cover
    def __init__(self, success=True): # pragma: no cover
        self._success = success # pragma: no cover
    def ok(self): # pragma: no cover
        if self._success: # pragma: no cover
            return 'transformed_line' # pragma: no cover
        else: # pragma: no cover
            return None # pragma: no cover
    def err(self): # pragma: no cover
        if not self._success: # pragma: no cover
            return CannotTransform('transformation error') # pragma: no cover
        else: # pragma: no cover
            return None # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def do_match(self, line): # pragma: no cover
        return MatchResult() # pragma: no cover
    def do_transform(self, line, indices): # pragma: no cover
        return [TransformResult()] # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

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
    _l_(17914)

    raise CannotTransform("There are no strings in this line.")
    _l_(17913)

match_result = self.do_match(line)
_l_(17915)

if isinstance(match_result, Err):
    _l_(17918)

    cant_transform = match_result.err()
    _l_(17916)
    raise CannotTransform(
        f"The string transformer {self.__class__.__name__} does not recognize"
        " this line as one that it can transform."
    ) from cant_transform
    _l_(17917)

string_indices = match_result.ok()
_l_(17919)

for line_result in self.do_transform(line, string_indices):
    _l_(17925)

    if isinstance(line_result, Err):
        _l_(17922)

        cant_transform = line_result.err()
        _l_(17920)
        raise CannotTransform(
            "StringTransformer failed while attempting to transform string."
        ) from cant_transform
        _l_(17921)
    line = line_result.ok()
    _l_(17923)
    aux = line
    _l_(17924)
    exit(aux)
