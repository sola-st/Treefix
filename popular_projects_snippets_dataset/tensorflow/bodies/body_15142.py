# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
# Apply static shape information saved in rt_spec to rt.
rt = rt_spec._from_components([flat_value, row_splits])
tester.assertEqual(rt.shape.as_list(), [2, None])
exit(rt + ragged_factory_ops.constant([[1.0, 1.0, 1.0], [1.0]]))
