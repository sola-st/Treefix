# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
"""Tests the test utility."""
original_lengths = [3, (3, 2, 8), 1]
original_rt = _to_prime_tensor_from_lengths(original_lengths)
expected_rt = _to_ragged_tensor_from_lengths(
    [[2], [3], [5], [7], [11], [13], [17], [19], [23], [29], [31], [37],
     [41]], [3, (3, 2, 8)])

self.assertAllEqual(expected_rt, original_rt)
