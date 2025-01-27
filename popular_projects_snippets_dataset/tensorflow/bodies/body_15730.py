# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_op_test.py
rt_inputs = self._rt_inputs_to_tensors(rt_inputs, ragged_ranks)
self.assertRaisesRegex(error, message, ragged_concat_ops.concat, rt_inputs,
                       axis)
