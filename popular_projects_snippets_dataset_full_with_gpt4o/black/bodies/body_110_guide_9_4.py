import token # pragma: no cover

def is_empty_par(leaf): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
class MockParser: # pragma: no cover
    LPAR = 'LPAR' # pragma: no cover
    RPAR = 'RPAR' # pragma: no cover
    DONE = 'DONE' # pragma: no cover
    DEFAULT_TOKEN = 'DEFAULT' # pragma: no cover
 # pragma: no cover
    def __init__(self): # pragma: no cover
        self._unmatched_lpars = 1 # pragma: no cover
        self._state = self.RPAR # pragma: no cover
        self._goto = { # pragma: no cover
            (self.RPAR, token.OP): self.DONE # pragma: no cover
        } # pragma: no cover
 # pragma: no cover
self = MockParser() # pragma: no cover

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
    _l_(19245)

    aux = True
    _l_(19244)
    exit(aux)

next_token = leaf.type
_l_(19246)
if next_token == token.LPAR:
    _l_(19248)

    self._unmatched_lpars += 1
    _l_(19247)

current_state = self._state
_l_(19249)

# The LPAR parser state is a special case. We will return True until we
# find the matching RPAR token.
if current_state == self.LPAR:
    _l_(19261)

    if next_token == token.RPAR:
        _l_(19253)

        self._unmatched_lpars -= 1
        _l_(19250)
        if self._unmatched_lpars == 0:
            _l_(19252)

            self._state = self.RPAR
            _l_(19251)
else:
    # If the lookup table matches the current state to the next
    # token, we use the lookup table.
    if (current_state, next_token) in self._goto:
        _l_(19258)

        self._state = self._goto[current_state, next_token]
        _l_(19254)
    else:
        # Otherwise, we check if a the current state was assigned a
        # default.
        if (current_state, self.DEFAULT_TOKEN) in self._goto:
            _l_(19257)

            self._state = self._goto[current_state, self.DEFAULT_TOKEN]
            _l_(19255)
        # If no default has been assigned, then this parser has a logic
        # error.
        else:
            raise RuntimeError(f"{self.__class__.__name__} LOGIC ERROR!")
            _l_(19256)

    if self._state == self.DONE:
        _l_(19260)

        aux = False
        _l_(19259)
        exit(aux)
aux = True
_l_(19262)

exit(aux)
