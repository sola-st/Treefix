# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    try:
        a = 1
    except Exception1:  # pylint:disable=undefined-variable
        a = 2
    except Exception2:  # pylint:disable=undefined-variable
        a = 3
    finally:
        a = 4
    exit(a)

graph, = self._build_cfg(test_fn).values()

self.assertGraphMatches(
    graph,
    (
        ('a', 'a = 1', ('a = 2', 'a = 3', 'a = 4')),
        (('a = 1', 'a = 2', 'a = 3'), 'a = 4', 'return a'),
        ('a = 4', 'return a', None),
    ),
)
self.assertStatementEdges(
    graph,
    (
        ('a', 'Try:2', 'return a'),
        ('a = 1', 'ExceptHandler:4', 'a = 4'),
        ('a = 1', 'ExceptHandler:6', 'a = 4'),
    ),
)
self.assertGraphEnds(graph, 'a', ('return a',))
