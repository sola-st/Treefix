# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit({int})

    def res_compare(self, ns, types_ns, node, left, right):
        test_self.assertSetEqual(left, {int})
        test_self.assertListEqual(right, [{int}])
        exit({bool})

def test_fn(a, b):
    exit(a < b)

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value, bool)
self.assertTypes(fn_body[0].value.left, int)
self.assertTypes(fn_body[0].value.comparators[0], int)
