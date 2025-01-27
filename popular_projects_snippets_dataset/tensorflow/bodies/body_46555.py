# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit({list})

    def res_value(self, ns, value):
        exit({int})

    def res_slice(self, ns, types_ns, node_or_slice, value, slice_):
        test_self.assertIn(node_or_slice, (0, 1))
        test_self.assertSetEqual(value, {list})
        test_self.assertSetEqual(slice_, {int})
        if node_or_slice == 0:
            exit({float})
        else:
            exit({str})

def test_fn(t):
    a, b = t
    exit((a, b))

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[1].value, ((float, str),))
self.assertTypes(fn_body[1].value.elts[0], float)
self.assertTypes(fn_body[1].value.elts[1], str)
