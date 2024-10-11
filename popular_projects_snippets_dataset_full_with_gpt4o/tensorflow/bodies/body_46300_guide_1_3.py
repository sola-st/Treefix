import ast # pragma: no cover
from unittest import TestCase, mock # pragma: no cover

class MockSelf: # pragma: no cover
    def _parse_and_analyze(self, fn): # pragma: no cover
        class MockNode: # pragma: no cover
            def __init__(self): # pragma: no cover
                self.body = [MockAnnAssignScopeNode()] # pragma: no cover
        return MockNode(), None # pragma: no cover
 # pragma: no cover
    def assertScopeIs(self, scope, symbols, annotations): # pragma: no cover
        print(f'assertScopeIs called with scope={scope}, symbols={symbols}, annotations={annotations}') # pragma: no cover
 # pragma: no cover
    def assertSymbolSetsAre(self, symbols, annotations, annotation_type): # pragma: no cover
        print(f'assertSymbolSetsAre called with symbols={symbols}, annotations={annotations}, annotation_type={annotation_type}') # pragma: no cover
 # pragma: no cover
class MockAnnAssignScopeNode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.scope = 'ann_assign_scope' # pragma: no cover
 # pragma: no cover
def mock_getanno(node, annotation_type): # pragma: no cover
    if annotation_type == NodeAnno.BODY_SCOPE: # pragma: no cover
        return mock.Mock(annotations=('b',)) # pragma: no cover
    elif annotation_type == anno.Static.SCOPE: # pragma: no cover
        return mock.Mock(annotations=('b',)) # pragma: no cover
 # pragma: no cover
class NodeAnno: # pragma: no cover
    BODY_SCOPE = 'body_scope' # pragma: no cover
 # pragma: no cover
class anno: # pragma: no cover
    Static = type('Static', (), {'SCOPE': 'scope'}) # pragma: no cover
 # pragma: no cover
anno.getanno = mock_getanno # pragma: no cover
self = MockSelf() # pragma: no cover

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
