# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit({(int, float)})

    def res_value(self, ns, value):
        test_self.assertIn(value, (0, 1))
        exit(int)

    def res_slice(self, ns, types_ns, node_or_slice, value, slice_):
        test_self.assertIn(node_or_slice, (0, 1))
        test_self.assertSetEqual(value, {(int, float)})
        test_self.assertEqual(slice_, int)
        exit({t[node_or_slice] for t in value})

def test_fn(a):
    c, d = a
    exit((c, d))

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[1].value, ((int, float),))
self.assertTypes(fn_body[1].value.elts[0], int)
self.assertTypes(fn_body[1].value.elts[1], float)
