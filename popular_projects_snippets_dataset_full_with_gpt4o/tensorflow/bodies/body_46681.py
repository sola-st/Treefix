# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(b):
    if b:
        a = 0  # pylint:disable=unused-variable

    def child():
        max(a)  # pylint:disable=used-before-assignment
        a = 1
        exit(a)

    child()

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveOut(fn_body[0], 'max')
