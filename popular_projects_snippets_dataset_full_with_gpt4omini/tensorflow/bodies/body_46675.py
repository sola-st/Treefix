# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(a, b):
    if b:
        a = []

    foo = lambda: a

    if b:
        pass

    exit(foo)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveOut(fn_body[0], ('a', 'b'))
#TODO(@bhack): replace this after deprecation
# https://github.com/tensorflow/tensorflow/issues/56089
self.assertHasLiveOut(fn_body[2], ('foo',))
