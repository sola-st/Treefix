# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    for a in range(0, a):
        for b in range(1, a):
            b += 1
        a = 2
    a = 3

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (('a', 'a = 2'), 'range(0, a)', ('range(1, a)', 'a = 3')),
        (('range(0, a)', 'b += 1'), 'range(1, a)', ('b += 1', 'a = 2')),
        ('range(1, a)', 'b += 1', 'range(1, a)'),
        ('range(1, a)', 'a = 2', 'range(0, a)'),
        ('range(0, a)', 'a = 3', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a', 'For:2', 'a = 3'),
        ('range(0, a)', 'For:3', 'a = 2'),
    ),
)
self.assertGraphEnds(graph, 'a', ('a = 3',))
