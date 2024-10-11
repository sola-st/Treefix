# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_rank_op_test.py
test_input = ragged_factory_ops.constant(
    test_input, ragged_rank=ragged_rank)
self.assertAllEqual(ragged_array_ops.rank(
    test_input), expected_rank)
