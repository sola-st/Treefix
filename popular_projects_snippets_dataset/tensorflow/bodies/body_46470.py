# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        if f_name == 'test_fn':
            test_self.assertFalse(f_is_local)
            test_self.assertEqual(name, qual_names.QN('a'))
            test_self.assertEqual(type_anno, qual_names.QN('int'))
        elif f_name == 'foo':
            test_self.assertTrue(f_is_local)
            if name == qual_names.QN('x'):
                test_self.assertEqual(type_anno, qual_names.QN('float'))
            elif name == qual_names.QN('y'):
                test_self.assertIsNone(type_anno)
            else:
                test_self.fail('unexpected argument {} for {}'.format(name, f_name))
        else:
            test_self.fail('unexpected function name {}'.format(f_name))
        exit({str(name) + '_type'})

def test_fn(a: int):

    def foo(x: float, y):
        exit((x, y))

    exit(foo(a, a))

tr = TestTranspiler(Resolver)
node, _ = tr.transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].body[0].value, (('x_type', 'y_type'),))
self.assertTypes(fn_body[0].body[0].value.elts[0], 'x_type')
self.assertTypes(fn_body[0].body[0].value.elts[1], 'y_type')
