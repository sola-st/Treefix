# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    while (lambda b: a + b)(a):
        pass

graphs = self._build_cfg(test_fn)
for k, v in graphs.items():
    if isinstance(k, gast.Lambda):
        lam_graph = v
    else:
        fn_graph = v

self.assertGraphMatches(
    fn_graph,
    (
        ('a', '(lambda b: (a + b))', '(lambda b: (a + b))(a)'),
        (('(lambda b: (a + b))', 'pass'), '(lambda b: (a + b))(a)', 'pass'),
        ('(lambda b: (a + b))(a)', 'pass', '(lambda b: (a + b))(a)'),
    ),
)
self.assertGraphEnds(fn_graph, 'a', ('(lambda b: (a + b))(a)',))
self.assertGraphMatches(
    lam_graph,
    (
        ('b', '(a + b)', None),
    ),
)
self.assertGraphEnds(lam_graph, 'b', ('(a + b)',))
