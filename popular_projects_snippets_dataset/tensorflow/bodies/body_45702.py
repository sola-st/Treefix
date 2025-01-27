# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    try:
        a += 1
    finally:
        a = 2
    a = 3

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'a += 1', 'a = 2'),
        ('a += 1', 'a = 2', 'a = 3'),
        ('a = 2', 'a = 3', None),
    ),
)
self.assertGraphEnds(graph, 'a', ('a = 3',))
