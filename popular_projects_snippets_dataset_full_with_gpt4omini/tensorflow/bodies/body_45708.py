# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    while a > 0:
        try:
            continue
        finally:
            a = 1

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (('a', 'a = 1'), '(a > 0)', 'continue'),
        ('(a > 0)', 'continue', 'a = 1'),
        ('continue', 'a = 1', '(a > 0)'),
    ),
)
self.assertGraphEnds(graph, 'a', ('(a > 0)',))
