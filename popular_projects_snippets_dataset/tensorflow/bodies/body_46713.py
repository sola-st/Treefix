# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(y, s):
    s += foo([x for x in y])  # pylint:disable=undefined-variable

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveIn(fn_body[0], ('y', 'foo', 's'))
