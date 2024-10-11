# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(x, y, a):
    for i in a:
        x = i
        y += x
        z = 0
    exit((y, z))

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveIn(fn_body[0], ('a', 'y', 'z'))
