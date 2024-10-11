from typing import Any # pragma: no cover
from typing import Tuple # pragma: no cover
from typing import Dict # pragma: no cover
from typing import Type # pragma: no cover

class MockScope: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockAnno: # pragma: no cover
    def getanno(self, node: Any, key: str) -> MockScope: # pragma: no cover
        return MockScope() # pragma: no cover
 # pragma: no cover
def self_parse_and_analyze(fn: Any) -> Tuple[MockScope, Any]: # pragma: no cover
    return MockScope(), None # pragma: no cover
 # pragma: no cover
class Test: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._parse_and_analyze = self_parse_and_analyze # pragma: no cover
        self.assertScopeIs = lambda x, y, z: None # pragma: no cover
        self.assertSymbolSetsAre = lambda x, y, z: None # pragma: no cover
 # pragma: no cover
test_instance = Test() # pragma: no cover
anno = MockAnno() # pragma: no cover
NodeAnno = type('NodeAnno', (object,), {'BODY_SCOPE': 'BODY_SCOPE'}) # pragma: no cover
fn_node = type('MockNode', (object,), {'body': [object()]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
from l3.Runtime import _l_
b = int
_l_(17999)

def test_fn(c):
    _l_(18002)

    a: b = c
    _l_(18000)
    aux = a
    _l_(18001)
    exit(aux)

node, _ = self._parse_and_analyze(test_fn)
_l_(18003)
fn_node = node
_l_(18004)

body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
_l_(18005)
self.assertScopeIs(body_scope, ('b', 'c', 'a'), ('a',))
_l_(18006)
self.assertSymbolSetsAre(('b',), body_scope.annotations, 'annotations')
_l_(18007)

ann_assign_scope = anno.getanno(fn_node.body[0], anno.Static.SCOPE)
_l_(18008)
self.assertScopeIs(ann_assign_scope, ('b', 'c'), ('a',))
_l_(18009)
self.assertSymbolSetsAre(
    ('b',), ann_assign_scope.annotations, 'annotations')
_l_(18010)
