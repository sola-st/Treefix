# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
root = autotrackable.AutoTrackable()
v1 = trackable_utils.add_variable(
    root, name="v1", initializer=3., dtype=dtypes.float64)
self.assertEqual(dtypes.float64, v1.dtype)
v2 = trackable_utils.add_variable(
    root,
    name="v2",
    shape=[3],
    initializer=init_ops.ones_initializer,
    dtype=dtypes.float64)
self.assertEqual(dtypes.float64, v2.dtype)
self.assertAllEqual([1., 1., 1.], self.evaluate(v2))
