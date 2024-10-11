# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def body():
    nonlocal i, s
    i = array_ops.ones(
        [random_ops.random_uniform(minval=1, maxval=4, shape=()), 7])
    s = math_ops.reduce_sum(i)

def set_state(loop_vars):
    nonlocal i, s
    i, s = loop_vars

i = variable_operators.Undefined('i')
s = constant_op.constant(0.0)
control_flow.while_stmt(
    test=lambda: math_ops.equal(s, 0),
    body=body,
    get_state=lambda: (i, s),
    set_state=set_state,
    symbol_names=('i', 's'),
    opts={})

self.assertEqual(i[0][0], 1)
self.assertGreaterEqual(s, 7)
self.assertOpCreated('While')  # Not stateless because of the random op.
