# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a):
    max(a)
    while True:
        a = a
        a = a
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

self.assertHasDefs(fn_body[0].value.args[0], 1)
self.assertHasDefs(fn_body[1].body[0].targets[0], 1)
self.assertHasDefs(fn_body[1].body[1].targets[0], 1)
self.assertHasDefs(fn_body[1].body[1].value, 1)
# The loop does have an invariant test, but the CFG doesn't know that.
self.assertHasDefs(fn_body[1].body[0].value, 2)
self.assertHasDefs(fn_body[2].value, 2)
