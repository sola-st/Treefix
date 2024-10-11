# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def test_fn(x: float):  # pylint:disable=unused-argument

    def foo():
        x = x + 1  # pylint:disable=used-before-assignment

    foo()

node, _ = TestTranspiler(BasicTestResolver).transform(test_fn, None)
fn_body = node.body

self.assertFalse(
    anno.hasanno(fn_body[0].body[0].value.left, anno.Static.TYPES))
self.assertClosureTypes(fn_body[0], {'x': {'float'}})
