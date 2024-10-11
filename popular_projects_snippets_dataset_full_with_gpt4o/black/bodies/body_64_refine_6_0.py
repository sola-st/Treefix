from typing import NamedTuple, List, Union # pragma: no cover

class CannotTransform(Exception):# pragma: no cover
    pass # pragma: no cover
line = type('MockLine', (object,), {'leaves': []})() # pragma: no cover
token = type('MockToken', (object,), {'STRING': 'string'})() # pragma: no cover
class Err(NamedTuple):# pragma: no cover
    err: callable# pragma: no cover
# pragma: no cover
class Ok(NamedTuple):# pragma: no cover
    ok: callable # pragma: no cover
self = type('MockSelf', (object,), {# pragma: no cover
    'do_match': lambda self, line: Ok(lambda: [0]),# pragma: no cover
    'do_transform': lambda self, line, indices: [Ok(lambda: line)]# pragma: no cover
})() # pragma: no cover

import token # pragma: no cover

line = type('MockLine', (object,), {'leaves': [type('MockLeaf', (object,), {'type': token.STRING})()]})() # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover
Err = type('Err', (object,), {'__init__': lambda self, err: setattr(self, 'err', err)}) # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'do_match': lambda self, line: type('MockMatchResult', (object,), { # pragma: no cover
        'ok': lambda self: [0], # pragma: no cover
        'err': lambda self: None # pragma: no cover
    })(), # pragma: no cover
    'do_transform': lambda self, line, indices: [type('MockLineResult', (object,), { # pragma: no cover
        'ok': lambda self: line, # pragma: no cover
        'err': lambda self: None # pragma: no cover
    })()] # pragma: no cover
})() # pragma: no cover

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
