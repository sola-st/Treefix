# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def test_fn(a: int, c: float):
    b = a
    exit((a, b, c))

node, _ = TestTranspiler(BasicTestResolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].targets[0], 'int')
self.assertTypes(fn_body[0].value, 'int')
self.assertTypes(fn_body[1].value.elts[0], 'int')
self.assertTypes(fn_body[1].value.elts[1], 'int')
self.assertTypes(fn_body[1].value.elts[2], 'float')
