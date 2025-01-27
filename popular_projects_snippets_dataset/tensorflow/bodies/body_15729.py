# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_op_test.py
rt_inputs = self._rt_inputs_to_tensors(rt_inputs, ragged_ranks)
concatenated = ragged_concat_ops.concat(rt_inputs, axis)
if expected_ragged_rank is not None:
    self.assertEqual(concatenated.ragged_rank, expected_ragged_rank)
if expected_shape is not None:
    self.assertEqual(concatenated.shape.as_list(), expected_shape)
self.assertAllEqual(concatenated, expected)
