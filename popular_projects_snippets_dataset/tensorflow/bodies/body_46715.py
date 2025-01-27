# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

def test_fn(y):
    if {x for x in y}:
        exit()

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasLiveIn(fn_body[0], ('y',))
