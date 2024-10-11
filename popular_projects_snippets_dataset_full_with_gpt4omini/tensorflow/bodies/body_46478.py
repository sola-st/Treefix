# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_value(self, ns, value):
        test_self.assertEqual(value, tc.a)
        exit({str})

    def res_name(self, ns, types_ns, name):
        test_self.assertEqual(name, qual_names.QN('tc'))
        exit(({TestClass}, tc))

    def res_call(self, ns, types_ns, node, f_type, args, keywords):
        test_self.assertEqual(f_type, (str,))
        exit(({int}, None))

class TestClass:

    def a(self):
        pass

tc = TestClass()

def test_fn():
    tc.a()

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertEqual(
    anno.getanno(fn_body[0].value.func, anno.Static.VALUE), tc.a)
self.assertTypes(fn_body[0].value.func, str)
self.assertTypes(fn_body[0].value, int)
self.assertTypes(fn_body[0], int)
