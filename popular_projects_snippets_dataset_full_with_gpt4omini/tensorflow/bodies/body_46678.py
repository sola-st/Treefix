# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(b):
    def foo(a):
        exit(a)

    if b:
        a = []  # pylint:disable=unused-variable

    exit(foo)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveOut(fn_body[1], ('foo'))
