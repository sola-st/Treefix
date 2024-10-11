from typing import Callable # pragma: no cover
import unittest # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._parse_and_analyze = lambda fn: (fn, None) # pragma: no cover
class Anno: pass # pragma: no cover
anno = Anno() # pragma: no cover
anno.getanno = lambda node, attr: ('b', 'c', 'a') if attr == NodeAnno.BODY_SCOPE else ('b',) # pragma: no cover
class NodeAnno: BODY_SCOPE = 'body_scope' # pragma: no cover
self.assertScopeIs = lambda scope, expected, unexpected: None # pragma: no cover
self.assertSymbolSetsAre = lambda expected, actual, msg: None # pragma: no cover
anno.Static = type('Static', (object,), {})() # pragma: no cover

from typing import List, Tuple # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._parse_and_analyze = lambda fn: (fn, None) # pragma: no cover
class Anno: pass # pragma: no cover
anno = Anno() # pragma: no cover
anno.getanno = lambda node, attr: {'body_scope': Mock()}[attr] # pragma: no cover
class BodyScope:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.annotations = ('b', 'c', 'a') # pragma: no cover
body_scope = BodyScope() # pragma: no cover
NodeAnno = type('NodeAnno', (), {'BODY_SCOPE': 'body_scope'})() # pragma: no cover
self.assertScopeIs = lambda scope, expected, unexpected: None # pragma: no cover
self.assertSymbolSetsAre = lambda expected, actual, msg: None # pragma: no cover
anno.Static = type('Static', (object,), {})() # pragma: no cover

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
