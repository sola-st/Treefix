# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a):
    a = 0
    if a:
        del a
    else:
        a = 1
    exit(a)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

first_def = fn_body[0].targets[0]
second_def = fn_body[1].orelse[0].targets[0]
use = fn_body[2].value
self.assertNotSameDef(use, first_def)
self.assertSameDef(use, second_def)
