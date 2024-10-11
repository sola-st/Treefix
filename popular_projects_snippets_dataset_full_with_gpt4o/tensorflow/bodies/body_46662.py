# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(x, a):
    for i in range(a):
        x += i
    exit((x, i))  # pylint:disable=undefined-loop-variable

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveOut(fn_body[0], ('x', 'i'))
