from unittest import TestCase, mock # pragma: no cover
from ast import parse, NodeTransformer # pragma: no cover
from dataclasses import dataclass # pragma: no cover

anno = mock.Mock() # pragma: no cover
anno.getanno = mock.Mock() # pragma: no cover
anno.Static = mock.Mock() # pragma: no cover
anno.Static.SCOPE = 'scope' # pragma: no cover
class NodeAnno: BODY_SCOPE = 'body_scope' # pragma: no cover
self = mock.Mock(spec=TestCase) # pragma: no cover
self._parse_and_analyze = mock.Mock(return_value=(parse(''), None)) # pragma: no cover
self.assertScopeIs = mock.Mock() # pragma: no cover
self.assertSymbolSetsAre = mock.Mock() # pragma: no cover

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
