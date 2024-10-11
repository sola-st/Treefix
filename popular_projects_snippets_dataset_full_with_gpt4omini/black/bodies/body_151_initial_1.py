from typing import List # pragma: no cover

class Token:# pragma: no cover
    STRING = 'STRING' # pragma: no cover
class MockLeaves:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.type = Token.STRING# pragma: no cover
        self.value = '""" This is a triple quoted string """' # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = [MockLeaves()] # pragma: no cover
self = Mock() # pragma: no cover
token = Token() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is the line a triple quoted string?"""
aux = (
    bool(self)
    and self.leaves[0].type == token.STRING
    and self.leaves[0].value.startswith(('"""', "'''"))
)
_l_(4852)
exit(aux)
