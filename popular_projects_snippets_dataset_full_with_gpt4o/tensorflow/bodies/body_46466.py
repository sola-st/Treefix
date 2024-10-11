# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        test_self.assertFalse(f_is_local)
        if name == qual_names.QN('a'):
            test_self.assertEqual(type_anno, qual_names.QN('int'))
        exit({str(name) + '_type'})

def test_fn(a: int, b):
    exit((a, b))

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value.elts[0], 'a_type')
self.assertTypes(fn_body[0].value.elts[1], 'b_type')
