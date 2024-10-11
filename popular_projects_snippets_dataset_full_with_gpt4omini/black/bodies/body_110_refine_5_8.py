from typing import Dict, Any # pragma: no cover

def is_empty_par(leaf): return leaf == '' or leaf is None # pragma: no cover
leaf = type('Leaf', (object,), {'type': 'LPAR'})() # pragma: no cover
token = type('Token', (object,), {'LPAR': 'LPAR', 'RPAR': 'RPAR'})() # pragma: no cover
self = type('MockParser', (object,), { # pragma: no cover
    '_unmatched_lpars': 0, # pragma: no cover
    '_state': 'LPAR', # pragma: no cover
    'LPAR': 'LPAR', # pragma: no cover
    'RPAR': 'RPAR', # pragma: no cover
    '_goto': {('LPAR', 'RPAR'): 'DONE'}, # pragma: no cover
    'DEFAULT_TOKEN': 'DEFAULT', # pragma: no cover
    '__class__': type('Mock', (), {}), # pragma: no cover
    'DONE': 'DONE' # pragma: no cover
})() # pragma: no cover

from typing import Dict, Any # pragma: no cover

def is_empty_par(leaf): return leaf.type in [None, ''] # pragma: no cover
class Token: LPAR = 'LPAR'; RPAR = 'RPAR' # pragma: no cover
token = Token() # pragma: no cover
class MockParser:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self._unmatched_lpars = 0 # pragma: no cover
        self._state = 'INITIAL' # pragma: no cover
        self.LPAR = 'LPAR' # pragma: no cover
        self.RPAR = 'RPAR' # pragma: no cover
        self._goto = {('INITIAL', 'LPAR'): 'LPAR_STATE'} # pragma: no cover
        self.DEFAULT_TOKEN = 'DEFAULT' # pragma: no cover
        self.DONE = 'DONE' # pragma: no cover
    def __class__(self): return MockParser # pragma: no cover
self = MockParser() # pragma: no cover
class MockLeaf:  # pragma: no cover
    def __init__(self, leaf_type): # pragma: no cover
        self.type = leaf_type # pragma: no cover
leaf = MockLeaf(token.LPAR) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Pre-conditions:
            * On the first call to this function, @leaf MUST be the leaf that
            was directly after the string leaf in question (e.g. if our target
            string is `line.leaves[i]` then the first call to this method must
            be `line.leaves[i + 1]`).
            * On the next call to this function, the leaf parameter passed in
            MUST be the leaf directly following @leaf.

        Returns:
            True iff @leaf is apart of the string's trailer.
        """
# We ignore empty LPAR or RPAR leaves.
if is_empty_par(leaf):
    _l_(7744)

    aux = True
    _l_(7743)
    exit(aux)

next_token = leaf.type
_l_(7745)
if next_token == token.LPAR:
    _l_(7747)

    self._unmatched_lpars += 1
    _l_(7746)

current_state = self._state
_l_(7748)

# The LPAR parser state is a special case. We will return True until we
# find the matching RPAR token.
if current_state == self.LPAR:
    _l_(7760)

    if next_token == token.RPAR:
        _l_(7752)

        self._unmatched_lpars -= 1
        _l_(7749)
        if self._unmatched_lpars == 0:
            _l_(7751)

            self._state = self.RPAR
            _l_(7750)
else:
    # If the lookup table matches the current state to the next
    # token, we use the lookup table.
    if (current_state, next_token) in self._goto:
        _l_(7757)

        self._state = self._goto[current_state, next_token]
        _l_(7753)
    else:
        # Otherwise, we check if a the current state was assigned a
        # default.
        if (current_state, self.DEFAULT_TOKEN) in self._goto:
            _l_(7756)

            self._state = self._goto[current_state, self.DEFAULT_TOKEN]
            _l_(7754)
        # If no default has been assigned, then this parser has a logic
        # error.
        else:
            raise RuntimeError(f"{self.__class__.__name__} LOGIC ERROR!")
            _l_(7755)

    if self._state == self.DONE:
        _l_(7759)

        aux = False
        _l_(7758)
        exit(aux)
aux = True
_l_(7761)

exit(aux)
