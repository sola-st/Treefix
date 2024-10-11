# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
v = self.variable('v', 0, dtypes.int32)

def body(i):
    v.assign(v.read_value() * 10 + i[0])

control_flow.for_stmt(
    ragged_factory_ops.constant([[1], [2, 4], [3]]),
    extra_test=None,
    body=body,
    get_state=lambda: (),
    set_state=lambda _: None,
    symbol_names=(),
    opts={})

# Note: 123 = ((0*10 + 1)*10+2)*10+3 (first element of each row).
self.assertEqual(v.read_value(), 123)
self.assertOpCreated('While')
