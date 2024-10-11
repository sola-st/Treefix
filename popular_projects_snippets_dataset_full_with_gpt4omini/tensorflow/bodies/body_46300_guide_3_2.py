from typing import Any # pragma: no cover
import anno # pragma: no cover

self = type('Mock', (object,), {'_parse_and_analyze': lambda fn: (fn, None), 'assertScopeIs': lambda scope, expected, unexpected: None, 'assertSymbolSetsAre': lambda expected, actual, msg: None})() # pragma: no cover
b = int # pragma: no cover
fn_node = type('MockNode', (object,), {'body': [None]})() # pragma: no cover
fn_node.body[0] = fn_node # pragma: no cover
anno.getanno = lambda node, anno_type: ('b', 'c', 'a') if anno_type == NodeAnno.BODY_SCOPE else ('b', 'c') # pragma: no cover
NodeAnno = type('NodeAnno', (), {'BODY_SCOPE': 'BODY_SCOPE'})() # pragma: no cover
body_scope = anno.getanno(fn_node, NodeAnno.BODY_SCOPE) # pragma: no cover

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
