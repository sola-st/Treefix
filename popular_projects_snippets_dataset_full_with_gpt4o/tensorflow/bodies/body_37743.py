# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
"""Test RaggedFeature with 3 partitions."""
original = [
    # rt shape: [(batch), 2, None, None]
    example(
        features=features({
            # rt = [[[[1]], [[2, 3], [4]]], [[], [[5, 6, 7]]]]
            "rt_values": float_feature([1, 2, 3, 4, 5, 6, 7]),
            "lengths_axis2": int64_feature([1, 2, 0, 1]),
            "lengths_axis3": int64_feature([1, 2, 1, 3]),
            "splits_axis3": int64_feature([0, 1, 3, 4, 7]),
        })),
    example(
        features=features({
            # rt = [[[[1, 2, 3], [4]], [[5], [6], [7, 8]]]]
            "rt_values": float_feature([1, 2, 3, 4, 5, 6, 7, 8]),
            "lengths_axis2": int64_feature([2, 3]),
            "lengths_axis3": int64_feature([3, 1, 1, 1, 2]),
            "splits_axis3": int64_feature([0, 3, 4, 5, 6, 8]),
        }))
]
serialized = ops.convert_to_tensor(
    [m.SerializeToString() for m in original])

test_features = {
    "rt1":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[
                parsing_ops.RaggedFeature.UniformRowLength(2),
                parsing_ops.RaggedFeature.RowLengths("lengths_axis2"),
                parsing_ops.RaggedFeature.RowSplits("splits_axis3"),
            ],
            dtype=dtypes.float32,
            row_splits_dtype=dtypes.int64,
        ),
}

expected_rt = ragged_factory_ops.constant(
    [[[[[1]], [[2, 3], [4]]], [[], [[5, 6, 7]]]],
     [[[[1, 2, 3], [4]], [[5], [6], [7, 8]]]]],
    dtype=dtypes.float32,
    row_splits_dtype=dtypes.int64)

expected_output = {
    "rt1": expected_rt,
}

self._test({
    "serialized": serialized,
    "features": test_features
}, expected_output)
