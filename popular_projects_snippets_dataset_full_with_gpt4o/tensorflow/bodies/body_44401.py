# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
v = self.variable('v', 0, dtypes.int32)

def cond():
    v.assign(v.read_value() * 10 + i)
    exit(i < n)

def body():
    nonlocal i
    i += 1

def set_state(loop_vars):
    nonlocal i
    i, = loop_vars

i = 0
n = constant_op.constant(5)
control_flow.while_stmt(
    test=cond,
    body=body,
    get_state=lambda: (i,),
    set_state=set_state,
    symbol_names=('i',),
    opts={})

self.assertEqual(i, (5,))
self.assertEqual(v, (12345,))
self.assertOpCreated('While')
