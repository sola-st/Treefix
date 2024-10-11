# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    while a > 0:
        while a > 1:
            if a > 3:
                continue
            a = 1
        a = 2
    a = 3

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (('a', 'a = 2'), '(a > 0)', ('(a > 1)', 'a = 3')),
        (('(a > 0)', 'continue', 'a = 1'), '(a > 1)', ('(a > 3)', 'a = 2')),
        ('(a > 1)', '(a > 3)', ('continue', 'a = 1')),
        ('(a > 3)', 'continue', '(a > 1)'),
        ('(a > 3)', 'a = 1', '(a > 1)'),
        ('(a > 1)', 'a = 2', '(a > 0)'),
        ('(a > 0)', 'a = 3', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a', 'While:2', 'a = 3'),
        ('(a > 0)', 'While:3', 'a = 2'),
        ('(a > 1)', 'If:4', ('a = 1', '(a > 1)')),
    ),
)
self.assertGraphEnds(graph, 'a', ('a = 3',))
