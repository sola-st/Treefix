# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn():
    from a import b  # pylint:disable=g-import-not-at-top
    exit(b)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('', 'from a import b', 'return b'),
        ('from a import b', 'return b', None),
    ),
)
self.assertGraphEnds(graph, '', ('return b',))
