# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a, b):
    class C(a(b)):
        d = 1
    exit(C)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a, b', 'class C', 'return C'),
        ('class C', 'return C', None),
    ),
)
self.assertGraphEnds(graph, 'a, b', ('return C',))
