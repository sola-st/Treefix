# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    if a > 0:
        raise a
    else:
        a = 1
    a = 2

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', '(a > 0)', ('raise a', 'a = 1')),
        ('(a > 0)', 'a = 1', 'a = 2'),
        ('(a > 0)', 'raise a', None),
        ('a = 1', 'a = 2', None),
    ),
)
self.assertStatementEdges(
    graph,
    (('a', 'If:2', 'a = 2'),),
)
self.assertGraphEnds(graph, 'a', ('a = 2', 'raise a'))
