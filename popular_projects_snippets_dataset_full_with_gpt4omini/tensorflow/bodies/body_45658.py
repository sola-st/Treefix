# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    if a > 0:
        if a > 1:
            a = 1
        else:
            a = 2
    else:
        if a > 2:
            a = 3
        else:
            a = 4

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (None, 'a', '(a > 0)'),
        ('a', '(a > 0)', ('(a > 1)', '(a > 2)')),
        ('(a > 0)', '(a > 1)', ('a = 1', 'a = 2')),
        ('(a > 1)', 'a = 1', None),
        ('(a > 1)', 'a = 2', None),
        ('(a > 0)', '(a > 2)', ('a = 3', 'a = 4')),
        ('(a > 2)', 'a = 3', None),
        ('(a > 2)', 'a = 4', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a', 'If:2', None),
        ('(a > 0)', 'If:3', None),
        ('(a > 0)', 'If:8', None),
    ),
)
self.assertGraphEnds(graph, 'a', ('a = 1', 'a = 2', 'a = 3', 'a = 4'))
