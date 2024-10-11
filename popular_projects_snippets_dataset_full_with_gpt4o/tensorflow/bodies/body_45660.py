# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    if a > 0:
        a = 1

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (None, 'a', '(a > 0)'),
        ('a', '(a > 0)', 'a = 1'),
        ('(a > 0)', 'a = 1', None),
    ),
)
self.assertStatementEdges(
    graph,
    (('a', 'If:2', None),),
)
self.assertGraphEnds(graph, 'a', ('(a > 0)', 'a = 1'))
