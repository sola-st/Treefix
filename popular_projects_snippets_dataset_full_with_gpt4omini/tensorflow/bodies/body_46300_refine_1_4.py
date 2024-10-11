from typing import Any # pragma: no cover
from unittest import TestCase # pragma: no cover
import anno # pragma: no cover

class NodeAnno: BODY_SCOPE = 'body_scope' # pragma: no cover
class Mock: # pragma: no cover
    def _parse_and_analyze(self, fn): # pragma: no cover
        return (fn, None)# pragma: no cover
    def assertScopeIs(self, scope, expected, unexpected): # pragma: no cover
        pass# pragma: no cover
    def assertSymbolSetsAre(self, expected, actual, label): # pragma: no cover
        pass# pragma: no cover
self = Mock() # pragma: no cover

from typing import Any # pragma: no cover
from unittest import TestCase # pragma: no cover

class NodeAnno: BODY_SCOPE = 'body_scope' # pragma: no cover
class anno:# pragma: no cover
    @staticmethod# pragma: no cover
    def getanno(node, anno_type):# pragma: no cover
        if anno_type == NodeAnno.BODY_SCOPE:# pragma: no cover
            return {'annotations': ('b', 'c', 'a')}# pragma: no cover
        return {} # pragma: no cover
class Mock:# pragma: no cover
    def _parse_and_analyze(self, fn):# pragma: no cover
        return (fn, None)# pragma: no cover
    def assertScopeIs(self, scope, expected, unexpected):# pragma: no cover
        pass# pragma: no cover
    def assertSymbolSetsAre(self, expected, actual, label):# pragma: no cover
        pass# pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
from l3.Runtime import _l_
b = int
_l_(5972)

def test_fn(c):
    _l_(5975)

    a: b = c
    _l_(5973)
    aux = a
    _l_(5974)
    exit(aux)

node, _ = self._parse_and_analyze(test_fn)
_l_(5976)
fn_node = node
_l_(5977)

body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE)
_l_(5978)
self.assertScopeIs(body_scope, ('b', 'c', 'a'), ('a',))
_l_(5979)
self.assertSymbolSetsAre(('b',), body_scope.annotations, 'annotations')
_l_(5980)

ann_assign_scope = anno.getanno(fn_node.body[0], anno.Static.SCOPE)
_l_(5981)
self.assertScopeIs(ann_assign_scope, ('b', 'c'), ('a',))
_l_(5982)
self.assertSymbolSetsAre(
    ('b',), ann_assign_scope.annotations, 'annotations')
_l_(5983)
