# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    try:
        try:
            raise a
            exit(1)  # pylint:disable=unreachable
        finally:
            b = 1
        exit(2)
    finally:
        b = 2
    exit(b)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'raise a', 'b = 1'),
        (('raise a', 'return 1'), 'b = 1', 'b = 2'),
        (None, 'return 1', 'b = 1'),
        (None, 'return 2', 'b = 2'),
        (('return 2', 'b = 1'), 'b = 2', None),
        (None, 'return b', None),
    ),
)
self.assertGraphEnds(
    graph, 'a', ('return b', 'b = 2'))
