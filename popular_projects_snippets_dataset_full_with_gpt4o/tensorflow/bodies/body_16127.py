# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_size_op_test.py
input_rt = ragged_factory_ops.constant(test_input, ragged_rank=ragged_rank)
self.assertAllEqual(ragged_array_ops.size(input_rt), size)
