# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

class MutableObject:
    field = constant_op.constant(0, dtype=dtypes.int32)
state = MutableObject()

def body():
    nonlocal i
    state.field = state.field * 10 + i
    i += 1

def set_state(loop_vars):
    nonlocal i
    i, state.field = loop_vars

i = 0
n = constant_op.constant(5)
control_flow.while_stmt(
    test=lambda: i < n,
    body=body,
    get_state=lambda: (i, state.field),
    set_state=set_state,
    symbol_names=('i', 'state.field'),
    opts={})

self.assertEqual(i, 5)
self.assertEqual(state.field, 1234)
self.assertOpCreated('StatelessWhile')
