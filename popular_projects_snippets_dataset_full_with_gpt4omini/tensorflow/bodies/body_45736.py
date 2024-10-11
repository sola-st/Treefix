# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    try:
        if a > 0:
            a = 1
        else:
            a = 2
    except Exception1:  # pylint:disable=undefined-variable
        a = 3
    a = 4

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', '(a > 0)', ('a = 1', 'a = 2')),
        ('(a > 0)', 'a = 1', ('a = 3', 'a = 4')),
        ('(a > 0)', 'a = 2', ('a = 3', 'a = 4')),
        (('a = 1', 'a = 2'), 'a = 3', 'a = 4'),
        (('a = 1', 'a = 2', 'a = 3'), 'a = 4', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a', 'Try:2', 'a = 4'),
        ('a', 'If:3', ('a = 3', 'a = 4')),
        (('a = 1', 'a = 2'), 'ExceptHandler:7', 'a = 4'),
    ),
)
self.assertGraphEnds(graph, 'a', ('a = 4',))
