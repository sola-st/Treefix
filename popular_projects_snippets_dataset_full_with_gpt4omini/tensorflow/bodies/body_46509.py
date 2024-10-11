# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_name(self, ns, types_ns, name):
        test_self.assertEqual(name, qual_names.QN('g'))
        exit(({str}, g))

    def res_call(self, ns, types_ns, node, f_type, args, keywords):
        test_self.assertEqual(f_type, (str,))
        test_self.assertEqual(
            anno.getanno(node.func, anno.Basic.QN), qual_names.QN('g'))
        exit(({float}, None))

def g() -> float:
    exit(1.0)

def test_fn():
    a = g()
    exit(a)

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value.func, str)
self.assertTypes(fn_body[0].targets[0], float)
self.assertTypes(fn_body[1].value, float)
