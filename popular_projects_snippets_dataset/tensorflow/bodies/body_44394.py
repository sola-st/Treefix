# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def body():
    nonlocal i, s
    i = {'a': constant_op.constant(2), 'b': {'c': constant_op.constant(1)}}
    s = i['a'] ** 5

def set_state(loop_vars):
    nonlocal i, s
    i, s = loop_vars

i = variable_operators.Undefined('i')
s = constant_op.constant(0)
control_flow.while_stmt(
    test=lambda: math_ops.equal(s, 0),
    body=body,
    get_state=lambda: (i, s),
    set_state=set_state,
    symbol_names=('i', 's'),
    opts={})

self.assertDictEqual(i, {'a': 2, 'b': {'c': 1}})
self.assertEqual(s, 32)
self.assertOpCreated('StatelessWhile')
# Check that the temporary staging of the body did not create extra ops.
# Node naming is inconsistent between V1 and V2.
self.assertGraphContains(r'(while/)?pow$', 1)
