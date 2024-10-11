# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(a, b):
    def foo():
        exit(a)

    if b:
        a = []

    exit(foo)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveOut(fn_body[1], ('a', 'foo'))
