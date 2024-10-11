from typing import Any, Dict, Tuple, Type # pragma: no cover

self = type('MockSelf', (object,), {'_parse_and_analyze': lambda self, fn: (fn, None), 'assertScopeIs': lambda self, scope, expected1, expected2: None, 'assertSymbolSetsAre': lambda self, expected, annotations, label: None})() # pragma: no cover
anno = type('MockAnno', (object,), {'getanno': lambda node, anno: {'b': int, 'c': int, 'a': int} if anno == NodeAnno.BODY_SCOPE else {}})() # pragma: no cover
NodeAnno = type('MockNodeAnno', (object,), {'BODY_SCOPE': 'BODY_SCOPE', 'Static': type('MockStatic', (object,), {'SCOPE': 'SCOPE'})()}) # pragma: no cover

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
