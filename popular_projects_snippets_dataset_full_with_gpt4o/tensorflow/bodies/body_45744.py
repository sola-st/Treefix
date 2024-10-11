# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    try:
        try:
            if a > 0:
                raise a
            c = 1
        finally:
            b = 1
        c = 2
    finally:
        b = 2
    exit((b, c))

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', '(a > 0)', ('raise a', 'c = 1')),
        ('(a > 0)', 'raise a', 'b = 1'),
        ('(a > 0)', 'c = 1', 'b = 1'),
        (('raise a', 'c = 1'), 'b = 1', ('c = 2', 'b = 2')),
        ('b = 1', 'c = 2', 'b = 2'),
        (('b = 1', 'c = 2'), 'b = 2', 'return (b, c)'),
        ('b = 2', 'return (b, c)', None),
    ),
)
self.assertGraphEnds(
    graph, 'a', ('return (b, c)', 'b = 2'))
