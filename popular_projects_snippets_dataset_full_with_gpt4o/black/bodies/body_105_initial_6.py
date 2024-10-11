from typing import List, Any # pragma: no cover

class MockToken: # pragma: no cover
    NAME = 1 # pragma: no cover
    EQUAL = 2 # pragma: no cover
    PLUSEQUAL = 3 # pragma: no cover
    STRING = 4 # pragma: no cover
    COMMA = 5 # pragma: no cover
 # pragma: no cover
class MockSyms: # pragma: no cover
    expr_stmt = 1 # pragma: no cover
    argument = 2 # pragma: no cover
    power = 3 # pragma: no cover
 # pragma: no cover
def parent_type(leaf): # pragma: no cover
    return MockSyms.expr_stmt  # or MockSyms.argument or MockSyms.power as needed # pragma: no cover
 # pragma: no cover
class StringParser: # pragma: no cover
    def parse(self, LL: List[Any], string_idx: int) -> int: # pragma: no cover
        # Example implementation, to increase the index; # pragma: no cover
        # replace this logic with actual string parsing logic if necessary. # pragma: no cover
        return string_idx + 1 # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(LL: List[Any]): # pragma: no cover
    def is_valid_index(idx: int) -> bool: # pragma: no cover
        return 0 <= idx < len(LL) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
def is_empty_par(element: Any) -> bool: # pragma: no cover
    return False  # Replace with actual logic to check if element is an empty parenthesis # pragma: no cover
 # pragma: no cover
LL = [type('Leaf', (object,), {'type': MockToken.NAME})()] # pragma: no cover
 # pragma: no cover
syms = MockSyms() # pragma: no cover
token = MockToken() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Returns:
            string_idx such that @LL[string_idx] is equal to our target (i.e.
            matched) string, if this line matches the assignment statement
            requirements listed in the 'Requirements' section of this classes'
            docstring.
                OR
            None, otherwise.
        """
# If this line is apart of an expression statement or is a function
# argument AND the first leaf contains a variable name...
if (
    parent_type(LL[0]) in [syms.expr_stmt, syms.argument, syms.power]
    and LL[0].type == token.NAME
):
    _l_(16066)

    is_valid_index = is_valid_index_factory(LL)
    _l_(16054)

    for i, leaf in enumerate(LL):
        _l_(16065)

        # We MUST find either an '=' or '+=' symbol...
        if leaf.type in [token.EQUAL, token.PLUSEQUAL]:
            _l_(16064)

            idx = i + 2 if is_empty_par(LL[i + 1]) else i + 1
            _l_(16055)

            # That symbol MUST be followed by a string...
            if is_valid_index(idx) and LL[idx].type == token.STRING:
                _l_(16063)

                string_idx = idx
                _l_(16056)

                # Skip the string trailer, if one exists.
                string_parser = StringParser()
                _l_(16057)
                idx = string_parser.parse(LL, string_idx)
                _l_(16058)

                # The next leaf MAY be a comma iff this line is apart
                # of a function argument...
                if (
                    parent_type(LL[0]) == syms.argument
                    and is_valid_index(idx)
                    and LL[idx].type == token.COMMA
                ):
                    _l_(16060)

                    idx += 1
                    _l_(16059)

                # But no more leaves are allowed...
                if not is_valid_index(idx):
                    _l_(16062)

                    aux = string_idx
                    _l_(16061)
                    exit(aux)
aux = None
_l_(16067)

exit(aux)
