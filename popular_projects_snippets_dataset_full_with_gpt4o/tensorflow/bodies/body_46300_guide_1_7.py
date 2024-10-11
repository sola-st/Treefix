import ast # pragma: no cover
from unittest.mock import Mock # pragma: no cover

def mock_parse_and_analyze(fn): # pragma: no cover
    tree = ast.parse(inspect.getsource(fn)) # pragma: no cover
    return tree.body[0], None # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self._parse_and_analyze = mock_parse_and_analyze # pragma: no cover
self.assertScopeIs = lambda scope, vars1, vars2: None # pragma: no cover
self.assertSymbolSetsAre = lambda vars, annotations, annotation: None # pragma: no cover
 # pragma: no cover
class MockAnno: # pragma: no cover
    def getanno(self, node, key): # pragma: no cover
        if key == NodeAnno.BODY_SCOPE: # pragma: no cover
            mock_scope = Mock() # pragma: no cover
            mock_scope.annotations = ('b',) # pragma: no cover
            return mock_scope # pragma: no cover
        elif key == StaticAnno.SCOPE: # pragma: no cover
            mock_scope = Mock() # pragma: no cover
            mock_scope.annotations = ('b',) # pragma: no cover
            return mock_scope # pragma: no cover
 # pragma: no cover
anno = MockAnno() # pragma: no cover
 # pragma: no cover
class NodeAnno: # pragma: no cover
    BODY_SCOPE = 'BODY_SCOPE' # pragma: no cover
 # pragma: no cover
class StaticAnno: # pragma: no cover
    SCOPE = 'SCOPE' # pragma: no cover

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
