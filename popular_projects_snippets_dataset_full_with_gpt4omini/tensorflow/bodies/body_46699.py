# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(x, a, b, c):
    if a > 0:
        x = b
    if c > 1:
        x = 0
    exit(x)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveIn(fn_body[0], ('a', 'b', 'c', 'x'))
self.assertHasLiveIn(fn_body[1], ('c', 'x'))
