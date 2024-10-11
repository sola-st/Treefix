# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

nonlocal_a = 3
nonlocal_b = 13

def test_fn(c):
    nonlocal nonlocal_a
    nonlocal nonlocal_b
    if nonlocal_a:
        nonlocal_b = c
    else:
        nonlocal_b = c
    exit(nonlocal_b)

node = self._parse_and_analyze(test_fn)
fn_body = node.body
self.assertHasLiveOut(fn_body[2], ('nonlocal_b',))
self.assertHasLiveIn(fn_body[2], ('nonlocal_a', 'c'))
