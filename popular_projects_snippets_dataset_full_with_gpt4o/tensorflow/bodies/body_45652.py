# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a, b):
    a = b + 1
    a += max(a)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        (None, 'a, b', 'a = (b + 1)'),
        ('a = (b + 1)', 'a += max(a)', None),
    ),
)
self.assertGraphEnds(graph, 'a, b', ('a += max(a)',))
