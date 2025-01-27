# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a, b):
    try:
        raise b
    except a:
        c = 1
    except b:
        c = 2
    finally:
        c += 3

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a, b', 'raise b', ('c = 1', 'c = 2', 'c += 3')),
        ('raise b', 'c = 1', 'c += 3'),
        ('raise b', 'c = 2', 'c += 3'),
        (('raise b', 'c = 1', 'c = 2'), 'c += 3', None),
    ),
)
self.assertGraphEnds(graph, 'a, b', ('c += 3',))
