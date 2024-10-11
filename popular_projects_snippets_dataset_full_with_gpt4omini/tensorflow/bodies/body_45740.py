# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a, b):
    raise b
    exit(a)  # pylint:disable=unreachable

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a, b', 'raise b', None),
        (None, 'return a', None),
    ),
)
self.assertGraphEnds(graph, 'a, b', ('raise b', 'return a'))
