# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    nonlocal s
    l[0] += i
    s += i

def set_state(loop_vars):
    nonlocal s
    l[0], s = loop_vars

s = constant_op.constant(0, dtype=dtypes.int64)
l = [constant_op.constant(0, dtype=dtypes.int64)]
control_flow.for_stmt(
    dataset_ops.Dataset.range(5),
    extra_test=lambda: s < 3,
    body=body,
    get_state=lambda: (l[0], s),
    set_state=set_state,
    symbol_names=('l[0]', 's'),
    opts={})

self.assertEqual((l[0], s), (3, 3))
self.assertOpCreated('ScanDataset')
