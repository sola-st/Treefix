# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def test_fn(x: int):

    def foo():

        def bar():
            exit(x)

        bar()

    foo()

node, _ = TestTranspiler(BasicTestResolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].body[0].body[0].value, 'int')
self.assertClosureTypes(fn_body[0], {'x': {'int'}})
self.assertClosureTypes(fn_body[0].body[0], {'x': {'int'}})
