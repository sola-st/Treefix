# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
original = [
    example(
        features=features({
            "rt_c": float_feature([3, 4, 5, 6, 7, 8]),
            "rt_f_values": float_feature([0, 1, 2, 3, 4]),
        })),
    example(
        features=features({
            "rt_c": float_feature([]),  # empty float list
        })),
    example(
        features=features({
            "rt_d": feature(),  # feature with nothing in it
        })),
    example(
        features=features({
            "rt_c": float_feature([1, 2, -1]),
            "rt_d": bytes_feature([b"hi"]),
            "rt_f_values": float_feature([0, 1, 2]),
        }))
]

serialized = [m.SerializeToString() for m in original]

expected_rt_c = ragged_factory_ops.constant_value(
    [[3.0, 4.0, 5.0, 6.0, 7.0, 8.0], [], [], [1.0, 2.0, -1.0]],
    row_splits_dtype=dtypes.int32)
expected_rt_d = ragged_factory_ops.constant_value(
    [[], [], [], [b"hi"]], row_splits_dtype=dtypes.int64)
expected_rt_f = ragged_factory_ops.constant_value(
    [[0.0, 1.0, 2.0, 3.0, 4.0], [], [], [0.0, 1.0, 2.0]],
    row_splits_dtype=dtypes.int32)

expected_output = {
    "rt_c": expected_rt_c,
    "rt_d": expected_rt_d,
    "rt_f": expected_rt_f,
}

self._test(
    ops.convert_to_tensor(serialized), {
        "rt_c":
            parsing_ops.RaggedFeature(dtypes.float32),
        "rt_d":
            parsing_ops.RaggedFeature(
                dtypes.string, row_splits_dtype=dtypes.int64),
        "rt_f":
            parsing_ops.RaggedFeature(
                dtypes.float32, value_key="rt_f_values"),
    },
    expected_values=expected_output,
    create_iterator_twice=True)
