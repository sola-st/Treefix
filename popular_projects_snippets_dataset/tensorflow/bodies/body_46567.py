# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit({list})

    def res_unop(self, ns, types_ns, node, opnd):
        exit({float})

def test_fn(a):
    exit(-a)

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value, float)
self.assertTypes(fn_body[0].value.operand, list)
