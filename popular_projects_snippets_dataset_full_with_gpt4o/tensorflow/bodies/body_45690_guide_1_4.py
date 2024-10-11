import unittest # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockBuilder(SimpleNamespace): # pragma: no cover
    def _build_cfg(self, fn): # pragma: no cover
        graph = SimpleNamespace(values=lambda: [{'graph': 'mock_graph'}.values()]) # pragma: no cover
        return {'graph': graph} # pragma: no cover
mock_instance = MockBuilder() # pragma: no cover
def mock_assertGraphMatches(graph, structure): # pragma: no cover
    print('Graph matches structure') # pragma: no cover
mock_instance.assertGraphMatches = mock_assertGraphMatches # pragma: no cover
def mock_assertStatementEdges(graph, edges): # pragma: no cover
    print('Statement edges match expected structure') # pragma: no cover
mock_instance.assertStatementEdges = mock_assertStatementEdges # pragma: no cover
def mock_assertGraphEnds(graph, start, end): # pragma: no cover
    print('Graph ends match expected structure') # pragma: no cover
mock_instance.assertGraphEnds = mock_assertGraphEnds # pragma: no cover
self = mock_instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

from l3.Runtime import _l_
def test_fn(a):
    _l_(19142)

    for a in range(0, a):
        _l_(19140)

        if a > 1:
            _l_(19137)

            break
            _l_(19136)
        a = 1
        _l_(19138)
    else:
        a = 2
        _l_(19139)
    a = 3
    _l_(19141)

graph, = self._build_cfg(test_fn).values()
_l_(19143)

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
_l_(19144)
self.assertStatementEdges(
    graph,
    (
        ('a', 'For:2', 'a = 3'),
        ('range(0, a)', 'If:3', ('a = 1', 'a = 3')),
    ),
)
_l_(19145)
self.assertGraphEnds(graph, 'a', ('a = 3',))
_l_(19146)
