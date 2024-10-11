# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    for a in range(0, a):
        a = 1
    else:  # pylint:disable=useless-else-on-loop
        a = 2
    a = 3

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (('a', 'a = 1'), 'range(0, a)', ('a = 1', 'a = 2')),
        ('range(0, a)', 'a = 1', 'range(0, a)'),
        ('range(0, a)', 'a = 2', 'a = 3'),
        ('a = 2', 'a = 3', None),
    ),
)
self.assertStatementEdges(
    graph,
    (('a', 'For:2', 'a = 3'),),
)
self.assertGraphEnds(graph, 'a', ('a = 3',))
