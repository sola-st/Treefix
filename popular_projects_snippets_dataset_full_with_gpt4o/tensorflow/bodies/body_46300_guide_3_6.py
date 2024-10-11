import ast # pragma: no cover
from unittest.mock import Mock # pragma: no cover
from unittest import TestCase # pragma: no cover

class MockSelf(TestCase): # pragma: no cover
    def _parse_and_analyze(self, fn): # pragma: no cover
        source = ''' # pragma: no cover
def test_fn(c): # pragma: no cover
    a: int = c # pragma: no cover
    aux = a # pragma: no cover
''' # pragma: no cover
        tree = ast.parse(source) # pragma: no cover
        return tree.body[0], None # pragma: no cover
 # pragma: no cover
    def assertScopeIs(self, scope, expected_defined, expected_referenced): # pragma: no cover
        print(f'assertScopeIs called with scope={scope}, expected_defined={expected_defined}, expected_referenced={expected_referenced}') # pragma: no cover
 # pragma: no cover
    def assertSymbolSetsAre(self, expected_symbols, actual_symbols, key): # pragma: no cover
        print(f'assertSymbolSetsAre called with expected_symbols={expected_symbols}, actual_symbols={actual_symbols}, key={key}') # pragma: no cover
 # pragma: no cover
class MockAnno: # pragma: no cover
    @staticmethod # pragma: no cover
    def getanno(node, key): # pragma: no cover
        if key == NodeAnno.BODY_SCOPE: # pragma: no cover
            body_scope_mock = Mock() # pragma: no cover
            body_scope_mock.annotations = ('b', 'c', 'a') # pragma: no cover
            return body_scope_mock # pragma: no cover
        elif key == StaticAnno.SCOPE: # pragma: no cover
            ann_assign_scope_mock = Mock() # pragma: no cover
            ann_assign_scope_mock.annotations = ('b', 'c') # pragma: no cover
            return ann_assign_scope_mock # pragma: no cover
 # pragma: no cover
class NodeAnno: # pragma: no cover
    BODY_SCOPE = 'BODY_SCOPE' # pragma: no cover
 # pragma: no cover
class StaticAnno: # pragma: no cover
    SCOPE = 'SCOPE' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
anno = MockAnno() # pragma: no cover
anno.Static = StaticAnno() # pragma: no cover

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
