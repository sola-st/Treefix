# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit({list})

    def res_value(self, ns, value):
        exit({int})

    def res_slice(self, ns, types_ns, node, value, slice_):
        test_self.assertSetEqual(value, {list})
        test_self.assertSetEqual(slice_, {int})
        exit({str})

def test_fn(a):
    exit(a[1])

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value, str)
self.assertTypes(fn_body[0].value.value, list)
self.assertTypes(fn_body[0].value.slice, int)
