# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    try:
        exit(a)
    finally:
        a = 1
    a = 2

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'return a', 'a = 1'),
        ('return a', 'a = 1', None),
        (None, 'a = 2', None),
    ),
)
# Note, `a = 1` executes after `return a`.
self.assertGraphEnds(graph, 'a', ('a = 2', 'a = 1'))
