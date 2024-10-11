# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_name(self, ns, types_ns, name):
        test_self.assertEqual(name, qual_names.QN('g'))
        exit((None, g))

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit({str(type_anno)})

    def res_call(self, ns, types_ns, node, f_type, args, keywords):
        test_self.assertIsNone(f_type)
        exit((None, {qual_names.QN('x'): {str}}))

def g():
    # The resolver will pretend that this function has the following body:
    #
    #   nonlocal x
    #   x = 'a'
    pass

def test_fn(x: int):
    y = x
    g()
    exit((x, y))

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].targets[0], 'int')
self.assertTypes(fn_body[0].value, 'int')
self.assertTypes(fn_body[2].value.elts[0], str)
self.assertTypes(fn_body[2].value.elts[1], 'int')
