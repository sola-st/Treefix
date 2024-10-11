# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
"""Test RaggedFeatures with nested partitions."""
original = [
    # rt shape: [(batch), 2, None, None]
    sequence_example(
        context=features({
            # a[0] = [[[[1]], [[2, 3], [4]]], [[], [[5, 6, 7]]]]
            "a_values": float_feature([1, 2, 3, 4, 5, 6, 7]),
            "a_lengths_axis2": int64_feature([1, 2, 0, 1]),
            "a_lengths_axis3": int64_feature([1, 2, 1, 3]),
            "a_splits_axis3": int64_feature([0, 1, 3, 4, 7])
        }),
        feature_lists=feature_lists({
            # b[0] = [[[1], [2, 3, 4]], [[2, 4], [6]]]
            "b_values":
                feature_list(
                    [float_feature([1, 2, 3, 4]),
                     float_feature([2, 4, 6])]),
            "b_splits":
                feature_list(
                    [int64_feature([0, 1, 4]),
                     int64_feature([0, 2, 3])]),
        })),
    sequence_example(
        # a[1] = []
        # b[1] = []
    ),
    sequence_example(
        context=features({
            # a[2] = [[[[1, 2, 3], [4]], [[5], [6], [7, 8]]]]
            "a_values": float_feature([1, 2, 3, 4, 5, 6, 7, 8]),
            "a_lengths_axis2": int64_feature([2, 3]),
            "a_lengths_axis3": int64_feature([3, 1, 1, 1, 2]),
            "a_splits_axis3": int64_feature([0, 3, 4, 5, 6, 8])
        }),
        feature_lists=feature_lists({
            # b[2] = [[[9], [8, 7, 6], [5]], [[4, 3, 2, 1]], [[0]]]
            "b_values":
                feature_list([
                    float_feature([9, 8, 7, 6, 5]),
                    float_feature([4, 3, 2, 1]),
                    float_feature([0])
                ]),
            "b_splits":
                feature_list([
                    int64_feature([0, 1, 4, 5]),
                    int64_feature([0, 4]),
                    int64_feature([0, 1])
                ])
        }))
]
serialized = [m.SerializeToString() for m in original]

context_features = {
    "a":
        parsing_ops.RaggedFeature(
            value_key="a_values",
            partitions=[
                parsing_ops.RaggedFeature.UniformRowLength(2),
                parsing_ops.RaggedFeature.RowLengths("a_lengths_axis2"),
                parsing_ops.RaggedFeature.RowSplits("a_splits_axis3"),
            ],
            dtype=dtypes.float32,
            row_splits_dtype=dtypes.int64,
        )
}
sequence_features = {
    "b":
        parsing_ops.RaggedFeature(
            value_key="b_values",
            dtype=dtypes.float32,
            partitions=[parsing_ops.RaggedFeature.RowSplits("b_splits")]),
    "c":
        parsing_ops.RaggedFeature(
            value_key="b_values",
            dtype=dtypes.float32,
            partitions=[parsing_ops.RaggedFeature.UniformRowLength(1)]),
}

expected_context = {
    "a":
        ragged_factory_ops.constant(
            [[[[[1]], [[2, 3], [4]]], [[], [[5, 6, 7]]]], [],
             [[[[1, 2, 3], [4]], [[5], [6], [7, 8]]]]],
            dtype=dtypes.float32,
            row_splits_dtype=dtypes.int64)
}
expected_feature_list = {
    "b":
        ragged_factory_ops.constant(
            [[[[1], [2, 3, 4]], [[2, 4], [6]]], [],
             [[[9], [8, 7, 6], [5]], [[4, 3, 2, 1]], [[0]]]],
            dtype=dtypes.float32,
            row_splits_dtype=dtypes.int32),
    "c":
        ragged_factory_ops.constant(
            [[[[1], [2], [3], [4]], [[2], [4], [6]]], [],
             [[[9], [8], [7], [6], [5]], [[4], [3], [2], [1]], [[0]]]],
            ragged_rank=2,
            dtype=dtypes.float32,
            row_splits_dtype=dtypes.int32),
}

self._test(
    dict(
        serialized=ops.convert_to_tensor(serialized),
        context_features=context_features,
        sequence_features=sequence_features),
    expected_context,
    expected_feature_list,
    batch=True)

self._test(
    dict(
        serialized=ops.convert_to_tensor(serialized)[0],
        context_features=context_features,
        sequence_features=sequence_features),
    {"a": expected_context["a"][0]}, {
        "b": expected_feature_list["b"][0],
        "c": expected_feature_list["c"][0]
    },
    batch=False)
