# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    try:
        a = 1
    except (Exception1, Exception2) as e:  # pylint:disable=undefined-variable,unused-variable
        a = 2
    exit(a)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'a = 1', ('a = 2', 'return a')),
        (('a = 1', 'a = 2'), 'return a', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a', 'Try:2', 'return a'),
        ('a = 1', 'ExceptHandler:4', 'return a'),
    ),
)
self.assertGraphEnds(graph, 'a', ('return a',))
