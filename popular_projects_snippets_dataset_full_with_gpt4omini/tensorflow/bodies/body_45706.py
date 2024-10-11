# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    while a > 0:
        try:
            break
        finally:
            a = 1

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', '(a > 0)', 'break'),
        ('(a > 0)', 'break', 'a = 1'),
        ('break', 'a = 1', None),
    ),
)
self.assertGraphEnds(graph, 'a', ('(a > 0)', 'a = 1'))
