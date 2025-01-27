# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py

def test_fn(a):
    l = []
    l[0] = a
    exit(l)

node = self._parse_and_analyze(test_fn)
fn_body = node.body

creation = fn_body[0].targets[0]
mutation = fn_body[1].targets[0].value
use = fn_body[2].value
self.assertSameDef(creation, mutation)
self.assertSameDef(creation, use)
