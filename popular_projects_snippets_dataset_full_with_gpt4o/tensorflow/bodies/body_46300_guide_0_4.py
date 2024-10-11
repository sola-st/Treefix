from typing import Any # pragma: no cover
from unittest import TestCase # pragma: no cover
from typing_extensions import Annotated # pragma: no cover

class MockSelf: # pragma: no cover
    def _parse_and_analyze(self, fn: Any) -> (Any, Any): # pragma: no cover
        return fn, None # pragma: no cover
 # pragma: no cover
    def assertScopeIs(self, scope, syms1, syms2): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
    def assertSymbolSetsAre(self, syms, annots, annotType): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class anno: # pragma: no cover
    @staticmethod # pragma: no cover
    def getanno(node: Any, arg: Any) -> Any: # pragma: no cover
        if arg == 'NodeAnno.BODY_SCOPE': # pragma: no cover
            return body_scope_result # pragma: no cover
        elif arg == 'anno.Static.SCOPE': # pragma: no cover
            return ann_assign_scope_result # pragma: no cover
 # pragma: no cover
class NodeAnno: # pragma: no cover
    BODY_SCOPE = 'NodeAnno.BODY_SCOPE' # pragma: no cover
 # pragma: no cover
class Static: # pragma: no cover
    SCOPE = 'anno.Static.SCOPE' # pragma: no cover
 # pragma: no cover

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
