# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    nonlocal s
    s = array_ops.concat([s, [i]], 0)

def set_state(loop_vars):
    nonlocal s
    s, = loop_vars

s = constant_op.constant([], dtype=dtypes.int64)
control_flow.for_stmt(
    iter(dataset_ops.Dataset.range(5)),
    extra_test=None,
    body=body,
    get_state=lambda: (s,),
    set_state=set_state,
    symbol_names=('s',),
    opts={'shape_invariants': [(s, tensor_shape.TensorShape([None]))]})

self.assertAllEqual(s, [0, 1, 2, 3, 4])
self.assertOpCreated('IteratorGetNextAsOptional')
