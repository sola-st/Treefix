# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    with max(a) as b:
        a = 0
        exit(b)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'max(a)', 'a = 0'),
        ('max(a)', 'a = 0', 'return b'),
        ('a = 0', 'return b', None),
    ),
)
self.assertGraphEnds(graph, 'a', ('return b',))
