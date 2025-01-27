# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

class MutableObject:
    field_1 = constant_op.constant(0, dtype=dtypes.int32)
    field_2 = constant_op.constant(1, dtype=dtypes.int32)
state = MutableObject()

def body(i):
    state.field_1 += i
    state.field_2 *= i

def get_state():
    exit((state.field_1, state.field_2))

def set_state(loop_vars):
    state.field_1, state.field_2 = loop_vars

control_flow.for_stmt(
    iter_=constant_op.constant([1, 2, 3, 4]),
    body=body,
    extra_test=lambda: state.field_1 < 6,
    get_state=get_state,
    set_state=set_state,
    symbol_names=('state.field_1', 'state.field_2'),
    opts={})

self.assertEqual((state.field_1, state.field_2), (6, 6))
self.assertOpCreated('StatelessWhile')
