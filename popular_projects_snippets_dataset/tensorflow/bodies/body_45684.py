# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    for a in range(0, a):
        a = 1
    a = 2

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (('a', 'a = 1'), 'range(0, a)', ('a = 1', 'a = 2')),
        ('range(0, a)', 'a = 1', 'range(0, a)'),
        ('range(0, a)', 'a = 2', None),
    ),
)
self.assertStatementEdges(
    graph,
    (('a', 'For:2', 'a = 2'),),
)
self.assertGraphEnds(graph, 'a', ('a = 2',))
