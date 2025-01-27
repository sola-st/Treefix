# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):  # pylint:disable=unused-argument
    pass

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'pass', None),
    ),
)
self.assertGraphEnds(graph, 'a', ('pass',))
