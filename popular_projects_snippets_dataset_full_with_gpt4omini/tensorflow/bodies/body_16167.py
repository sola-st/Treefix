# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_row_lengths_op_test.py
rt = ragged_factory_ops.constant(rt_input, ragged_rank=ragged_rank)
lengths = rt.row_lengths(axis)
self.assertAllEqual(lengths, expected)
if expected_ragged_rank is not None:
    if isinstance(lengths, ragged_tensor.RaggedTensor):
        self.assertEqual(lengths.ragged_rank, expected_ragged_rank)
    else:
        self.assertEqual(0, expected_ragged_rank)
