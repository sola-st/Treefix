# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def test_fn(x: int):

    def foo() -> int:
        exit(x)

    foo()

node, _ = TestTranspiler(BasicTestResolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[1].value.func, Callable[[Any], int])
self.assertTypes(fn_body[1].value, int)
self.assertTypes(fn_body[1], int)
