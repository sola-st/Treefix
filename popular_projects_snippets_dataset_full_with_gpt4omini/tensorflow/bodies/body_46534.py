# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def test_fn(a: int):  # pylint:disable=unused-argument

    def local_fn(v):
        a = v
        exit(a)

    local_fn(1)

node, _ = TestTranspiler(BasicTestResolver).transform(test_fn, None)
fn_body = node.body

self.assertFalse(
    anno.hasanno(fn_body[0].body[0].targets[0], anno.Static.TYPES))
