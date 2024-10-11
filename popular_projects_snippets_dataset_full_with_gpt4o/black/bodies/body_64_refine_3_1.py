from typing import Any, Union, List # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class MockResult: # pragma: no cover
    _value: Any # pragma: no cover
     # pragma: no cover
    def __init__(self, value: Any): # pragma: no cover
        self._value = value # pragma: no cover
     # pragma: no cover
    def ok(self) -> Any: # pragma: no cover
        return self._value # pragma: no cover
     # pragma: no cover
    def err(self) -> Any: # pragma: no cover
        return Exception('An error occurred') # pragma: no cover
     # pragma: no cover
class MockTransformer: # pragma: no cover
    def do_match(self, line) -> Union[MockResult, 'Err']: # pragma: no cover
        # Always return ok with indices for simplicity # pragma: no cover
        return MockResult([0]) # pragma: no cover
     # pragma: no cover
    def do_transform(self, line, indices) -> List[Union[MockResult, 'Err']]: # pragma: no cover
        # Always return ok for simplicity # pragma: no cover
        return [MockResult(line)] # pragma: no cover
     # pragma: no cover
class MockToken: # pragma: no cover
    STRING = 'string' # pragma: no cover
     # pragma: no cover
# Define the variables # pragma: no cover
line = type('Line', (object,), {'leaves': [type('Leaf', (object,), {'type': MockToken.STRING})()]})() # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover
self = MockTransformer() # pragma: no cover
Err = MockResult('error') # pragma: no cover
token = MockToken() # pragma: no cover

from typing import Any, Union, List # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class MockResult: # pragma: no cover
    _value: Any # pragma: no cover
     # pragma: no cover
    def __init__(self, value: Any): # pragma: no cover
        self._value = value # pragma: no cover
     # pragma: no cover
    def ok(self) -> Any: # pragma: no cover
        return self._value # pragma: no cover
     # pragma: no cover
    def err(self) -> Any: # pragma: no cover
        return Exception('An error occurred') # pragma: no cover
     # pragma: no cover
class Err(MockResult): # pragma: no cover
    pass # pragma: no cover
     # pragma: no cover
class MockTransformer: # pragma: no cover
    def do_match(self, line) -> Union[MockResult, Err]: # pragma: no cover
        # Always return ok with indices for simplicity # pragma: no cover
        return MockResult([0]) # pragma: no cover
     # pragma: no cover
    def do_transform(self, line, indices) -> List[Union[MockResult, Err]]: # pragma: no cover
        # Always return ok for simplicity # pragma: no cover
        return [MockResult(line)] # pragma: no cover
     # pragma: no cover
class MockToken: # pragma: no cover
    STRING = 'string' # pragma: no cover
     # pragma: no cover
# Define the variables # pragma: no cover
line = type('Line', (object,), {'leaves': [type('Leaf', (object,), {'type': MockToken.STRING})()]})() # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover
self = MockTransformer() # pragma: no cover
token = MockToken() # pragma: no cover

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
