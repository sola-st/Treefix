# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    a += 1
    a = 2
    a = 3
    exit()

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (None, 'a', 'a += 1'),
        ('a += 1', 'a = 2', 'a = 3'),
        ('a = 2', 'a = 3', 'return'),
        ('a = 3', 'return', None),
    ),
)
self.assertGraphEnds(graph, 'a', ('return',))
