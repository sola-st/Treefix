# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit(None)

def test_fn(a, b):
    exit((a < b, a - b))

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

# With no information on operand types, the operators will infer nothing.
self.assertFalse(
    anno.hasanno(fn_body[0].value.elts[0], anno.Static.TYPES))
self.assertFalse(
    anno.hasanno(fn_body[0].value.elts[1], anno.Static.TYPES))
