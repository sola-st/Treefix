# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = sequence_example(
    feature_lists=feature_lists({
        "a":
            feature_list([
                int64_feature([-1, 0, 1]),
                int64_feature([2, 3, 4]),
                int64_feature([5, 6, 7]),
                int64_feature([8, 9, 10]),
            ]),
        "b":
            feature_list([bytes_feature([b"r00", b"r01", b"r10", b"r11"])]),
        "c":
            feature_list([float_feature([3, 4]),
                          float_feature([-1, 2])]),
    }))

serialized = original.SerializeToString()

expected_feature_list_output = {
    "a":
        np.array(
            [  # outer dimension is time.
                [[-1, 0, 1]],  # inside are 1x3 matrices
                [[2, 3, 4]],
                [[5, 6, 7]],
                [[8, 9, 10]]
            ],
            dtype=np.int64),
    "b":
        np.array(
            [  # outer dimension is time, inside are 2x2 matrices
                [[b"r00", b"r01"], [b"r10", b"r11"]]
            ],
            dtype=bytes),
    "c":
        np.array(
            [  # outer dimension is time, inside are 2-vectors
                [3, 4], [-1, 2]
            ],
            dtype=np.float32),
    "d":
        np.empty(shape=(0, 5), dtype=np.float32),  # empty_allowed_missing
}

self._testBoth(
    {
        "example_name": "in1",
        "serialized": ops.convert_to_tensor(serialized),
        "sequence_features": {
            "a":
                parsing_ops.FixedLenSequenceFeature((1, 3), dtypes.int64),
            "b":
                parsing_ops.FixedLenSequenceFeature((2, 2), dtypes.string),
            "c":
                parsing_ops.FixedLenSequenceFeature(2, dtypes.float32),
            "d":
                parsing_ops.FixedLenSequenceFeature(
                    (5,), dtypes.float32, allow_missing=True),
        }
    },
    expected_feat_list_values=expected_feature_list_output)
