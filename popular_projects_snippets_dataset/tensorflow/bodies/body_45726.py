# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    try:
        a = 1
        a = 2
    except Exception1:  # pylint:disable=undefined-variable
        a = 3
    exit(a)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'a = 1', 'a = 2'),
        ('a = 2', 'a = 3', 'return a'),
        (('a = 2', 'a = 3'), 'return a', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a', 'Try:2', 'return a'),
        ('a = 2', 'ExceptHandler:5', 'return a'),
    ),
)
self.assertGraphEnds(graph, 'a', ('return a',))
