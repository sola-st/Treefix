from typing import Any # pragma: no cover
from typing import Dict # pragma: no cover
from typing import Tuple # pragma: no cover
class NodeAnno: # pragma: no cover
    BODY_SCOPE = 'BODY_SCOPE' # pragma: no cover
class anno: # pragma: no cover
    @staticmethod # pragma: no cover
    def getanno(node: Any, key: str) -> Dict: # pragma: no cover
        return getattr(node, key, {}) # pragma: no cover

class MockObject: # pragma: no cover
    def __init__(self, **kwargs): # pragma: no cover
        for key, value in kwargs.items(): # pragma: no cover
            setattr(self, key, value) # pragma: no cover
node = MockObject(body=[MockObject()]) # pragma: no cover
_ = None # pragma: no cover
node.body[0].anno = {'Static.SCOPE': MockObject()} # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_parse_and_analyze': lambda self, fn: (node, _), # pragma: no cover
    'assertScopeIs': lambda self, scope, vars1, vars2: print(f'assertScopeIs called with {scope}, {vars1}, {vars2}'), # pragma: no cover
    'assertSymbolSetsAre': lambda self, vars, annotations, key: print(f'assertSymbolSetsAre called with {vars}, {annotations}, {key}') # pragma: no cover
}) # pragma: no cover

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
