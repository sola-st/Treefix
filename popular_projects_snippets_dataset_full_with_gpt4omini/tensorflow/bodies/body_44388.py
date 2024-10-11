# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def body():
    nonlocal i, y
    i += 1
    y = random_ops.random_uniform([i])

def set_state(loop_vars):
    nonlocal i, y
    i, y = loop_vars

i = constant_op.constant(0)
y = variable_operators.Undefined('y')
control_flow.while_stmt(
    test=lambda: math_ops.less(i, 3),
    body=body,
    get_state=lambda: (i, y),
    set_state=set_state,
    symbol_names=('i', 'y'),
    opts={})

self.assertEqual(i, 3)
self.assertLess(y[0], 3)
