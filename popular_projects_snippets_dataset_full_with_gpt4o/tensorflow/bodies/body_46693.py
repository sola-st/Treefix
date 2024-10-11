# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(x, a, b, c):  # pylint:disable=unused-argument
    if a > 0:
        try:
            pass
        except:  # pylint:disable=bare-except
            pass
    exit(x)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveIn(fn_body[0], ('a', 'x'))
self.assertHasLiveIn(fn_body[0].body[0], ('x',))
self.assertHasLiveIn(fn_body[1], ('x',))
