# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    exit()
    a += 1  # pylint:disable=unreachable

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (None, 'a', 'return'),
        ('a', 'return', None),
        (None, 'a += 1', None),
    ),
)
self.assertGraphEnds(graph, 'a', ('return', 'a += 1'))
