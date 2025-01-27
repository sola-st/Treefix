# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    v.assign(v.read_value() * 10 + i)

v = self.variable('v', 0, dtypes.int64)

control_flow.for_stmt(
    dataset_ops.Dataset.range(5),
    extra_test=None,
    body=body,
    get_state=lambda: (),
    set_state=lambda _: None,
    symbol_names=(),
    opts={})

self.assertEqual(v.read_value(), 1234)
self.assertOpCreated('ScanDataset')
