from typing import List # pragma: no cover

class MockToken: AT = '@'  # Assuming AT represents a decorator symbol # pragma: no cover
class MockLeaf: type = '@'  # Mocking a leaf with type that matches token.AT # pragma: no cover
class MockSelf: leaves: List[MockLeaf] = [MockLeaf()]  # MockSelf has a leaves attribute containing a single MockLeaf # pragma: no cover
self = MockSelf() # pragma: no cover
token = MockToken() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this line a decorator?"""
aux = bool(self) and self.leaves[0].type == token.AT
_l_(6925)
exit(aux)
