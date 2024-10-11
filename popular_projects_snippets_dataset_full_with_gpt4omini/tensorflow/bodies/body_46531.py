# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def test_fn(x: int):

    def foo():
        exit(x)

    x = 1.0
    foo()

node, _ = TestTranspiler(BasicTestResolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].body[0].value, float)
self.assertTypes(fn_body[1].targets[0], float)
self.assertClosureTypes(fn_body[0], {'x': {float}})
