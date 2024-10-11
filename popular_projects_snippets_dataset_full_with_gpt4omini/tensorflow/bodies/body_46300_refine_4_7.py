from unittest.mock import MagicMock # pragma: no cover

self = MagicMock() # pragma: no cover
anno = MagicMock() # pragma: no cover
NodeAnno = MagicMock() # pragma: no cover

from unittest.mock import MagicMock # pragma: no cover

self = MagicMock() # pragma: no cover
self._parse_and_analyze = MagicMock(return_value=(MagicMock(), None)) # pragma: no cover
anno = MagicMock() # pragma: no cover
NodeAnno = MagicMock() # pragma: no cover
NodeAnno.BODY_SCOPE = 'BODY_SCOPE' # pragma: no cover
self.assertScopeIs = MagicMock() # pragma: no cover
self.assertSymbolSetsAre = MagicMock() # pragma: no cover
anno.getanno = MagicMock(side_effect=lambda node, key: {'BODY_SCOPE': MagicMock(annotations=('b', 'c', 'a')), 'SCOPE': MagicMock() if key == 'SCOPE' else None}[key]) # pragma: no cover
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
