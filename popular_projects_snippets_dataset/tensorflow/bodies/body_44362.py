# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    nonlocal s
    nonlocal t
    s = array_ops.concat([s, [i]], 0)
    t = Test(var=t.var + 1)

def set_state(loop_vars):
    nonlocal s
    nonlocal t
    s, t = loop_vars

s = constant_op.constant([], dtype=dtypes.int64)
Test = collections.namedtuple('Test', ['var'])
t = Test(var=constant_op.constant([0], dtype=dtypes.int64))
control_flow.for_stmt(
    iter(dataset_ops.Dataset.range(5)),
    extra_test=None,
    body=body,
    get_state=lambda: (s, t),
    set_state=set_state,
    symbol_names=('s', 't'),
    opts={'shape_invariants': [(s, tensor_shape.TensorShape([None]))]})

self.assertAllEqual(s, [0, 1, 2, 3, 4])
self.assertEqual(t.var, [5])
self.assertOpCreated('IteratorGetNextAsOptional')
