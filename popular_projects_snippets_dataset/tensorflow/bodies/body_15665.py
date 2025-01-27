# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_expand_dims_op_test.py
rt = ragged_factory_ops.constant(rt_input, ragged_rank=ragged_rank)
expanded = ragged_array_ops.expand_dims(rt, axis=axis)
self.assertEqual(expanded.shape.ndims, rt.shape.ndims + 1)
if expected_shape is not None:
    self.assertEqual(expanded.shape.as_list(), expected_shape)

self.assertAllEqual(expanded, expected)
