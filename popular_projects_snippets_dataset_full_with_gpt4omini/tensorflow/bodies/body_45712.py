# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    a = lambda b: a + b
    exit(a)

graphs = self._build_cfg(test_fn)
for k, v in graphs.items():
    if isinstance(k, gast.Lambda):
        lam_graph = v
    else:
        fn_graph = v

self.assertGraphMatches(
    fn_graph,
    (
        ('a', '(lambda b: (a + b))', 'a = (lambda b: (a + b))'),
        ('(lambda b: (a + b))', 'a = (lambda b: (a + b))', 'return a'),
        ('a = (lambda b: (a + b))', 'return a', None),
    ),
)
self.assertGraphEnds(fn_graph, 'a', ('return a',))
self.assertGraphMatches(
    lam_graph,
    (
        ('b', '(a + b)', None),
    ),
)
self.assertGraphEnds(lam_graph, 'b', ('(a + b)',))
