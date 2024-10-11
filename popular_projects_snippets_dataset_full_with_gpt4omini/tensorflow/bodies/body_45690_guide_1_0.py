import unittest # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class TestGraph(unittest.TestCase): # pragma: no cover
    def _build_cfg(self, func): # pragma: no cover
        return {func: MagicMock()} # pragma: no cover
    def assertGraphMatches(self, graph, expected): # pragma: no cover
        pass # pragma: no cover
    def assertStatementEdges(self, graph, expected): # pragma: no cover
        pass # pragma: no cover
    def assertGraphEnds(self, graph, end_var, expected): # pragma: no cover
        pass # pragma: no cover
self = TestGraph() # pragma: no cover
test_fn = lambda a: None # pragma: no cover
graph, = self._build_cfg(test_fn).values() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

from l3.Runtime import _l_
def test_fn(a):
    _l_(6533)

    for a in range(0, a):
        _l_(6531)

        if a > 1:
            _l_(6528)

            break
            _l_(6527)
        a = 1
        _l_(6529)
    else:
        a = 2
        _l_(6530)
    a = 3
    _l_(6532)

graph, = self._build_cfg(test_fn).values()
_l_(6534)

self.assertGraphMatches(
    graph,
    (
        (('a', 'a = 1'), 'range(0, a)', ('(a > 1)', 'a = 2')),
        ('range(0, a)', '(a > 1)', ('break', 'a = 1')),
        ('(a > 1)', 'break', 'a = 3'),
        ('(a > 1)', 'a = 1', 'range(0, a)'),
        ('range(0, a)', 'a = 2', 'a = 3'),
        (('break', 'a = 2'), 'a = 3', None),
    ),
)
_l_(6535)
self.assertStatementEdges(
    graph,
    (
        ('a', 'For:2', 'a = 3'),
        ('range(0, a)', 'If:3', ('a = 1', 'a = 3')),
    ),
)
_l_(6536)
self.assertGraphEnds(graph, 'a', ('a = 3',))
_l_(6537)
