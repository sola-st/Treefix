# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
i = constant_op.constant(0)
x = ragged_factory_ops.constant([[[1, 2], [3], [4, 5, 6]],
                                 [[], [8, 9, 10]]])
c = lambda i, _: i < 10
def b(i, x):
    exit([
        i + 1,
        array_ops.concat([x, x[..., i:i+1]], axis=-1)
    ])
_, r = control_flow_ops.while_loop(c, b, [i, x])
self.assertEqual(r.row_splits.shape.as_list(), [3])
self.assertIn(r.values.row_splits.shape.as_list(), ([6], [None]))
self.assertIn(r.values.values.shape.as_list(), ([49], [None]))
