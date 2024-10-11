import ast # pragma: no cover

anno = type('MockAnno', (object,), {'getanno': lambda *args, **kwargs: 'mock_scope_data', 'Static': type('Static', (object,), {'SCOPE': 'mock_scope_data'})()})() # pragma: no cover
NodeAnno = type('MockNodeAnno', (object,), {'BODY_SCOPE': 'mock_body_scope'})() # pragma: no cover

import ast # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._parse_and_analyze = self._mock_parse_and_analyze # pragma: no cover
        self.assertScopeIs = lambda *args: None # pragma: no cover
        self.assertSymbolSetsAre = lambda *args: None # pragma: no cover
 # pragma: no cover
    def _mock_parse_and_analyze(self, fn): # pragma: no cover
        return node, None # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
class MockAnno: # pragma: no cover
    @staticmethod # pragma: no cover
    def getanno(node, anno_type): # pragma: no cover
        if anno_type == NodeAnno.BODY_SCOPE: # pragma: no cover
            return type('MockScope', (object,), {'annotations': set(['b', 'c', 'a'])})() # pragma: no cover
        else: # pragma: no cover
            return type('MockScope', (object,), {'annotations': set(['b'])})() # pragma: no cover
 # pragma: no cover
anno = MockAnno() # pragma: no cover
 # pragma: no cover
class MockNodeAnno: # pragma: no cover
    BODY_SCOPE = 'body_scope' # pragma: no cover
 # pragma: no cover
NodeAnno = MockNodeAnno() # pragma: no cover
 # pragma: no cover
anno.Static = type('StaticMock', (object,), {'SCOPE': 'scope'}) # pragma: no cover

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
