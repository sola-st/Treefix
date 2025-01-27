# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(a, b):
    if b:
        a = []

    def foo():
        exit(a)

    foo()

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveOut(fn_body[0], 'a')
