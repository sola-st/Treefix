# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    c = [b for b in a]
    exit(c)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'c = [b for b in a]', 'return c'),
        ('c = [b for b in a]', 'return c', None),
    ),
)
self.assertGraphEnds(graph, 'a', ('return c',))
