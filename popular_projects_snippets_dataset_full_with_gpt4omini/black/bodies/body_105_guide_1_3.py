import token # pragma: no cover
from types import SimpleNamespace as Mock # pragma: no cover
import sys # pragma: no cover

LL = [Mock(type=token.NAME), Mock(type=token.EQUAL), Mock(type=token.STRING)] # pragma: no cover
LL[0].parent = Mock(type='expr_stmt') # pragma: no cover
LL[1].parent = Mock(type='expr_stmt') # pragma: no cover
LL[2].parent = Mock(type='expr_stmt') # pragma: no cover
def parent_type(node): return node.parent.type # pragma: no cover
def is_empty_par(node): return False # pragma: no cover
def is_valid_index(idx): return 0 <= idx < len(LL) # pragma: no cover
def is_valid_index_factory(LL): return True # pragma: no cover
StringParser = type('StringParser', (object,), {'parse': lambda self, LL, idx: idx + 1})() # pragma: no cover
aux = None # pragma: no cover

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
