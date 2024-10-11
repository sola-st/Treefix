# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# Check that keyword-only arguments are sorted appropriately, so that they
# feed the right tensor into each input.
@polymorphic_function.function
def g(**kwargs):
    exit(string_ops.reduce_join(
        string_ops.reduce_join(
            ops.convert_to_tensor(sorted(kwargs.items())),
            axis=1,
            separator='='),
        axis=0,
        separator=', '))

s = constant_op.constant('s')
g.get_concrete_function(q=s, a=s, p=s, r=s, v=s, m=s, l=s)
self.assertAllEqual(
    g(m='a', r='b', v='c', q='d', l='e', a='f', p='g'),
    b'a=f, l=e, m=a, p=g, q=d, r=b, v=c')
self.assertAllEqual(
    g(q='d', a='f', p='g', r='b', v='c', m='a', l='e'),
    b'a=f, l=e, m=a, p=g, q=d, r=b, v=c')
self.assertAllEqual(
    g(a='f', l='e', m='a', p='g', q='d', r='b', v='c'),
    b'a=f, l=e, m=a, p=g, q=d, r=b, v=c')
