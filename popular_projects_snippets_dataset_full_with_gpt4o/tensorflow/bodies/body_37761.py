# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
first = sequence_example(
    feature_lists=feature_lists({
        "a":
            feature_list([
                int64_feature([-1, 0, 1]),
                int64_feature([2, 3, 4]),
                int64_feature([5, 6, 7]),
                int64_feature([8, 9, 10]),
            ])
    }))
second = sequence_example(
    context=features({"c": float_feature([7])}),
    feature_lists=feature_lists({
        "a": feature_list([
            int64_feature([21, 2, 11]),
        ]),
        "b": feature_list([
            int64_feature([5]),
        ]),
    }))

serialized = [first.SerializeToString(), second.SerializeToString()]

expected_context_output = {
    "c": np.array([-1, 7], dtype=np.float32),
}
expected_feature_list_output = {
    "a":
        np.array(
            [  # outermost dimension is example id
                [  # middle dimension is time.
                    [[-1, 0, 1]],  # inside are 1x3 matrices
                    [[2, 3, 4]],
                    [[5, 6, 7]],
                    [[8, 9, 10]]
                ],
                [  # middle dimension is time.
                    [[21, 2, 11]],  # inside are 1x3 matrices
                    [[0, 0, 0]],  # additional entries are padded with 0
                    [[0, 0, 0]],
                    [[0, 0, 0]]
                ]
            ],
            dtype=np.int64),
    "b":
        np.array([[0], [5]], dtype=np.int64),
    "d":
        np.empty(shape=(2, 0, 5), dtype=np.float32),  # allowed_missing
}

self._test(
    {
        "example_names": ops.convert_to_tensor(["in1", "in2"]),
        "serialized": ops.convert_to_tensor(serialized),
        "context_features": {
            "c":
                parsing_ops.FixedLenFeature(
                    (), dtypes.float32, default_value=-1),
        },
        "sequence_features": {
            "a":
                parsing_ops.FixedLenSequenceFeature((1, 3), dtypes.int64),
            "b":
                parsing_ops.FixedLenSequenceFeature(
                    (), dtypes.int64, allow_missing=True),
            "d":
                parsing_ops.FixedLenSequenceFeature(
                    (5,), dtypes.float32, allow_missing=True),
        }
    },
    expected_context_values=expected_context_output,
    expected_feat_list_values=expected_feature_list_output,
    expected_length_values={
        "a": [4, 1],
        "b": [0, 1],
        "d": [0, 0]
    },
    batch=True)
