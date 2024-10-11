# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
original = [
    example(
        features=features({
            # rt = [[3], [4, 5, 6]]
            "rt_values": float_feature([3, 4, 5, 6]),
            "rt_splits": int64_feature([0, 1, 4]),
            "rt_lengths": int64_feature([1, 3]),
            "rt_starts": int64_feature([0, 1]),
            "rt_limits": int64_feature([1, 4]),
            "rt_rowids": int64_feature([0, 1, 1, 1]),
        })),
    example(
        features=features({
            # rt = []
            "rt_values": float_feature([]),
            "rt_splits": int64_feature([0]),
            "rt_lengths": int64_feature([]),
            "rt_starts": int64_feature([]),
            "rt_limits": int64_feature([]),
            "rt_rowids": int64_feature([]),
        })),
    example(
        features=features({
            # rt = []
            "rt_values": feature(),  # feature with nothing in it
            "rt_splits": int64_feature([0]),
            "rt_lengths": feature(),
            "rt_starts": feature(),
            "rt_limits": feature(),
            "rt_rowids": feature(),
        })),
    example(
        features=features({
            # rt = [[1.0, 2.0, -1.0], [], [8.0, 9.0], [5.0]]
            "rt_values": float_feature([1, 2, -1, 8, 9, 5]),
            "rt_splits": int64_feature([0, 3, 3, 5, 6]),
            "rt_lengths": int64_feature([3, 0, 2, 1]),
            "rt_starts": int64_feature([0, 3, 3, 5]),
            "rt_limits": int64_feature([3, 3, 5, 6]),
            "rt_rowids": int64_feature([0, 0, 0, 2, 2, 3]),
        }))
]
serialized = [m.SerializeToString() for m in original]

test_features = {
    "rt1":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.RowSplits("rt_splits")],
            dtype=dtypes.float32),
    "rt2":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.RowLengths("rt_lengths")],
            dtype=dtypes.float32),
    "rt3":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.RowStarts("rt_starts")],
            dtype=dtypes.float32),
    "rt4":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.RowLimits("rt_limits")],
            dtype=dtypes.float32),
    "rt5":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.ValueRowIds("rt_rowids")],
            dtype=dtypes.float32),
    "uniform1":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[parsing_ops.RaggedFeature.UniformRowLength(2)],
            dtype=dtypes.float32),
    "uniform2":
        parsing_ops.RaggedFeature(
            value_key="rt_values",
            partitions=[
                parsing_ops.RaggedFeature.UniformRowLength(2),
                parsing_ops.RaggedFeature.RowSplits("rt_splits")
            ],
            dtype=dtypes.float32),
}

expected_rt = ragged_factory_ops.constant(
    [[[3], [4, 5, 6]], [], [], [[1, 2, -1], [], [8, 9], [5]]],
    dtype=dtypes.float32,
    row_splits_dtype=dtypes.int32)

expected_uniform1 = ragged_factory_ops.constant(
    [[[3, 4], [5, 6]], [], [], [[1, 2], [-1, 8], [9, 5]]],
    ragged_rank=1,
    dtype=dtypes.float32,
    row_splits_dtype=dtypes.int32)

expected_uniform2 = ragged_factory_ops.constant(
    [[[[3], [4, 5, 6]]], [], [], [[[1, 2, -1], []], [[8, 9], [5]]]],
    dtype=dtypes.float32,
    row_splits_dtype=dtypes.int32)

expected_output = {
    "rt1": expected_rt,
    "rt2": expected_rt,
    "rt3": expected_rt,
    "rt4": expected_rt,
    "rt5": expected_rt,
    "uniform1": expected_uniform1,
    "uniform2": expected_uniform2,
}

self._test(
    ops.convert_to_tensor(serialized),
    test_features,
    expected_values=expected_output,
    create_iterator_twice=True)
