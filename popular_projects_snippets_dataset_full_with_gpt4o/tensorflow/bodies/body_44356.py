# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    nonlocal s
    s = s * 10 + i

def set_state(loop_vars):
    nonlocal s
    s, = loop_vars

s = constant_op.constant(0, dtype=dtypes.int64)
control_flow.for_stmt(
    iter(dataset_ops.Dataset.range(5)),
    extra_test=None,
    body=body,
    get_state=lambda: (s,),
    set_state=set_state,
    symbol_names=('s',),
    opts={})

self.assertEqual(s, 1234)
self.assertOpCreated('IteratorGetNextAsOptional')
