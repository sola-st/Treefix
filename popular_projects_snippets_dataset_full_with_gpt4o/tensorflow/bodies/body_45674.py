# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    while a > 0:
        if a > 1:
            break
        a = 1
    else:
        a = 2
    a = 3

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (('a', 'a = 1'), '(a > 0)', ('(a > 1)', 'a = 2')),
        ('(a > 0)', '(a > 1)', ('break', 'a = 1')),
        ('(a > 1)', 'break', 'a = 3'),
        ('(a > 1)', 'a = 1', '(a > 0)'),
        ('(a > 0)', 'a = 2', 'a = 3'),
        (('break', 'a = 2'), 'a = 3', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a', 'While:2', 'a = 3'),
        ('(a > 0)', 'If:3', ('a = 1', 'a = 3')),
    ),
)
self.assertGraphEnds(graph, 'a', ('a = 3',))
