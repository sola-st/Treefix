# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
value = sequence_example(
    context=features({
        "global_feature": float_feature([1, 2, 3]),
    }),
    feature_lists=feature_lists({
        "repeated_feature_2_frames":
            feature_list([
                bytes_feature([b"a", b"b", b"c"]),
                bytes_feature([b"a", b"d", b"e"])
            ]),
        "repeated_feature_3_frames":
            feature_list([
                int64_feature([3, 4, 5, 6, 7]),
                int64_feature([-1, 0, 0, 0, 0]),
                int64_feature([1, 2, 3, 4, 5])
            ])
    }))
value.SerializeToString()  # Smoke test
