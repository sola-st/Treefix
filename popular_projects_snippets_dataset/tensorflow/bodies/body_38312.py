# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
"""Test for github #46897."""
ops_list = [
    math_ops.sparse_segment_sum,
    math_ops.sparse_segment_mean,
    math_ops.sparse_segment_sqrt_n,
]
for op in ops_list:
    with self.assertRaisesRegex(
        (ValueError, errors_impl.InvalidArgumentError),
        "Shape must be at least rank 1"):
        op(data=1.0, indices=[0], segment_ids=[3])
