# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a, b):
    try:
        if a > 0:
            raise b
        else:
            exit(0)
    except b:
        exit(1)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a, b', '(a > 0)', ('raise b', 'return 0')),
        ('(a > 0)', 'raise b', 'return 1'),
        ('(a > 0)', 'return 0', None),
        ('raise b', 'return 1', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a, b', 'Try:2', None),
        ('a, b', 'If:3', 'return 1'),
        ('raise b', 'ExceptHandler:7', None),
    ),
)
self.assertGraphEnds(graph, 'a, b', ('return 0', 'return 1', 'raise b'))
