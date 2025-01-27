# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(x, y, a):
    for i in a:
        for j in i:
            x = i
            y += x
            z = j
    exit((y, z))

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveIn(fn_body[0], ('a', 'y', 'z'))
