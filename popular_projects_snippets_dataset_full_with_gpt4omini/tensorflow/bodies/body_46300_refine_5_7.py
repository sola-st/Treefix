from typing import Any, Callable # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._parse_and_analyze = lambda fn: (fn, None) # pragma: no cover
class anno:  # pragma: no cover
    @staticmethod # pragma: no cover
    def getanno(node, value): return Mock() # pragma: no cover
    class Static: pass # pragma: no cover
    Static.SCOPE = 1 # pragma: no cover
class NodeAnno:  # pragma: no cover
    BODY_SCOPE = 1 # pragma: no cover
self.assertScopeIs = lambda scope, expected, unexpected: None # pragma: no cover
self.assertSymbolSetsAre = lambda expected, actual, msg: None # pragma: no cover

from unittest.mock import MagicMock # pragma: no cover

self = MagicMock() # pragma: no cover
self._parse_and_analyze = lambda fn: (fn, None) # pragma: no cover
anno = MagicMock() # pragma: no cover
anno.getanno = lambda node, attr: MagicMock(annotations=('b', 'c', 'a')) if attr == 'BODY_SCOPE' else None # pragma: no cover
NodeAnno = MagicMock() # pragma: no cover
NodeAnno.BODY_SCOPE = 'BODY_SCOPE' # pragma: no cover
self.assertScopeIs = lambda scope, expected, unexpected: None # pragma: no cover
self.assertSymbolSetsAre = lambda expected, actual, msg: None # pragma: no cover
anno.Static = MagicMock() # pragma: no cover

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
