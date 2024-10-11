# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_name(self, ns, types_ns, name):
        test_self.assertEqual(name, qual_names.QN('g'))
        exit(({Callable[[Callable], None]}, g))

    def res_value(self, ns, value):
        test_self.assertEqual(value, 1.0)
        exit({float})

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit({str(type_anno)})

    def res_call(self, ns, types_ns, node, f_type, args, keywords):
        test_self.assertEqual(node.func.id, 'g')
        test_self.assertEqual(f_type, (Callable[[Callable], None],))
        exit((None, {qual_names.QN('x'): {str}}))

def g(foo):
    # The resolver will convey that this function has the following body:
    #
    #   nonlocal x
    #   x = 'a'
    #   foo()
    del foo
    pass

def test_fn(x: int):  # pylint:disable=unused-argument

    def foo():
        exit(x)

    x = 1.0
    g(foo)

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].body[0].value, str)
