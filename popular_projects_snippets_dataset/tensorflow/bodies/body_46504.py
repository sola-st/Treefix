# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

a = 'foo'

def test_fn():
    b = a
    exit(b)

node, _ = TestTranspiler(BasicTestResolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].targets[0], str)
self.assertTypes(fn_body[1].value, str)
