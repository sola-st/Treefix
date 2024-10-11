from typing import List, Optional, Any # pragma: no cover
import token # pragma: no cover

def parent_type(node): return syms.expr_stmt # pragma: no cover
LL = [{ 'type': token.NAME }, { 'type': token.EQUAL }, { 'type': token.STRING, 'value': 'example' }, { 'type': token.COMMA }] # pragma: no cover
syms = type('Mock', (object,), { 'expr_stmt': 1, 'argument': 2, 'power': 3 })() # pragma: no cover
token = type('Mock', (object,), { 'NAME': 1, 'EQUAL': 2, 'PLUSEQUAL': 3, 'STRING': 4, 'COMMA': 5 })() # pragma: no cover
def is_valid_index_factory(LL): return lambda idx: idx >= 0 and idx < len(LL) # pragma: no cover
def is_empty_par(leaf): return False # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class MockNode:  # Create a mock class for the nodes# pragma: no cover
    def __init__(self, node_type):# pragma: no cover
        self.type = node_type # pragma: no cover
def parent_type(node): return 'expr_stmt' # pragma: no cover
LL = [MockNode(token.NAME), MockNode(token.EQUAL), MockNode(token.STRING), MockNode(token.COMMA)] # pragma: no cover
class syms:  # Define symbols for expression types# pragma: no cover
    expr_stmt = 'expr_stmt'# pragma: no cover
    argument = 'argument'# pragma: no cover
    power = 'power' # pragma: no cover
class token:  # Define mock token types# pragma: no cover
    NAME = 'NAME'# pragma: no cover
    EQUAL = 'EQUAL'# pragma: no cover
    PLUSEQUAL = 'PLUSEQUAL'# pragma: no cover
    STRING = 'STRING'# pragma: no cover
    COMMA = 'COMMA' # pragma: no cover
def is_valid_index_factory(LL): return lambda idx: 0 <= idx < len(LL) # pragma: no cover
def is_empty_par(node): return False # pragma: no cover
class StringParser:# pragma: no cover
    def parse(self, LL, index):# pragma: no cover
        return index + 1 # pragma: no cover

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
    _l_(4172)

    is_valid_index = is_valid_index_factory(LL)
    _l_(4160)

    for i, leaf in enumerate(LL):
        _l_(4171)

        # We MUST find either an '=' or '+=' symbol...
        if leaf.type in [token.EQUAL, token.PLUSEQUAL]:
            _l_(4170)

            idx = i + 2 if is_empty_par(LL[i + 1]) else i + 1
            _l_(4161)

            # That symbol MUST be followed by a string...
            if is_valid_index(idx) and LL[idx].type == token.STRING:
                _l_(4169)

                string_idx = idx
                _l_(4162)

                # Skip the string trailer, if one exists.
                string_parser = StringParser()
                _l_(4163)
                idx = string_parser.parse(LL, string_idx)
                _l_(4164)

                # The next leaf MAY be a comma iff this line is apart
                # of a function argument...
                if (
                    parent_type(LL[0]) == syms.argument
                    and is_valid_index(idx)
                    and LL[idx].type == token.COMMA
                ):
                    _l_(4166)

                    idx += 1
                    _l_(4165)

                # But no more leaves are allowed...
                if not is_valid_index(idx):
                    _l_(4168)

                    aux = string_idx
                    _l_(4167)
                    exit(aux)
aux = None
_l_(4173)

exit(aux)
