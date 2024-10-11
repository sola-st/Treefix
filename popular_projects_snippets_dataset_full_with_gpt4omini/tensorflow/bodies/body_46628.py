# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a):
    if a:
        a = 0
    else:
        a = 1
    del a
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

use = fn_body[2].value
self.assertHasDefs(use, 0)
