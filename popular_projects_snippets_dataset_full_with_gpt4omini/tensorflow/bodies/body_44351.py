# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(it):
    nonlocal i
    with ops.control_dependencies((control_flow_ops.Assert(i < 3, (i,)),)):
        i = it

def set_state(loop_vars):
    nonlocal i
    i, = loop_vars

i = constant_op.constant(0, dtype=dtypes.int64)
control_flow.for_stmt(
    dataset_ops.Dataset.range(5),
    extra_test=lambda: i < 3,
    body=body,
    get_state=lambda: (i,),
    set_state=set_state,
    symbol_names=('i',),
    opts={})

self.assertEqual(i, (3,))
self.assertOpCreated('ScanDataset')
