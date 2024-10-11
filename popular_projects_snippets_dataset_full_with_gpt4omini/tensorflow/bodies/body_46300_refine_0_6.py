from typing import Callable, Any # pragma: no cover

self = type('Mock', (), { '_parse_and_analyze': lambda fn: (fn, None), 'assertScopeIs': lambda a, b, c: None, 'assertSymbolSetsAre': lambda a, b, c: None })() # pragma: no cover
anno = type('Mock', (), { 'getanno': lambda node, anno_type: {'BODY_SCOPE': type('Mock', (), {'annotations': ('b', 'c', 'a')})(), 'Static': type('Mock', (), {})()}[anno_type], 'Static': type('Mock', (), {})() })() # pragma: no cover
NodeAnno = type('Mock', (), { 'BODY_SCOPE': 'BODY_SCOPE' })() # pragma: no cover

from typing import Callable, Any # pragma: no cover

NodeAnno = type('Mock', (), { 'BODY_SCOPE': 'BODY_SCOPE' })() # pragma: no cover

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
