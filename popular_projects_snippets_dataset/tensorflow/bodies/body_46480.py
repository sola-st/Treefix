# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def test_fn(a: int, b: float):
    c = a
    c = b
    exit(c)

node, _ = TestTranspiler(BasicTestResolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].targets[0], 'int')
self.assertTypes(fn_body[0].value, 'int')
self.assertTypes(fn_body[1].targets[0], 'float')
self.assertTypes(fn_body[1].value, 'float')
