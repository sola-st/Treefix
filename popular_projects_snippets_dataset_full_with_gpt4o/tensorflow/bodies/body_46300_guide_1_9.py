import ast # pragma: no cover
from unittest import TestCase, mock # pragma: no cover

class MockSelf(TestCase): # pragma: no cover
    def _parse_and_analyze(self, fn): # pragma: no cover
        fn_ast = ast.parse(inspect.getsource(fn), mode='exec') # pragma: no cover
        return fn_ast.body[0], None # pragma: no cover
    def assertScopeIs(self, scope, *args): # pragma: no cover
        pass # pragma: no cover
    def assertSymbolSetsAre(self, expected, actual, set_name): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
def mock_getanno(node, key): # pragma: no cover
    if key == 'BODY_SCOPE': # pragma: no cover
        return type('Scope', (object,), {'annotations': ('b',)})() # pragma: no cover
    elif key == 'scope': # pragma: no cover
        return type('Scope', (object,), {'annotations': ('b',)})() # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
anno = mock.Mock() # pragma: no cover
anno.getanno = mock_getanno # pragma: no cover
NodeAnno = type('NodeAnno', (object,), {'BODY_SCOPE': 'BODY_SCOPE'}) # pragma: no cover
anno.Static = type('Static', (object,), {'SCOPE': 'scope'}) # pragma: no cover

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
