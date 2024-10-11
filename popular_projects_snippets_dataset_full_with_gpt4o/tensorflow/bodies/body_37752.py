# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = sequence_example(
    feature_lists=feature_lists({
        "a":
            feature_list([int64_feature([3, 4]),
                          int64_feature([1, 0])]),
        "st_a":
            feature_list([
                float_feature([3.0, 4.0]),
                float_feature([5.0]),
                float_feature([])
            ]),
        "st_b":
            feature_list([
                bytes_feature([b"a"]),
                bytes_feature([]),
                bytes_feature([]),
                bytes_feature([b"b", b"c"])
            ])
    }))

serialized = original.SerializeToString()

expected_st_a = (
    np.array([[0, 0], [0, 1], [1, 0]], dtype=np.int64),  # indices
    np.array([3.0, 4.0, 5.0], dtype=np.float32),  # values
    np.array([3, 2], dtype=np.int64))  # shape: num_time = 3, max_feat = 2

expected_st_b = (
    np.array([[0, 0], [3, 0], [3, 1]], dtype=np.int64),  # indices
    np.array(["a", "b", "c"], dtype="|S"),  # values
    np.array([4, 2], dtype=np.int64))  # shape: num_time = 4, max_feat = 2

expected_st_c = (
    np.empty((0, 2), dtype=np.int64),  # indices
    np.empty((0,), dtype=np.int64),  # values
    np.array([0, 0], dtype=np.int64))  # shape: num_time = 0, max_feat = 0

expected_feature_list_output = {
    "a": np.array([[3, 4], [1, 0]], dtype=np.int64),
    "st_a": expected_st_a,
    "st_b": expected_st_b,
    "st_c": expected_st_c,
}

self._testBoth(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "sequence_features": {
            "st_a": parsing_ops.VarLenFeature(dtypes.float32),
            "st_b": parsing_ops.VarLenFeature(dtypes.string),
            "st_c": parsing_ops.VarLenFeature(dtypes.int64),
            "a": parsing_ops.FixedLenSequenceFeature((2,), dtypes.int64),
        }
    },
    expected_feat_list_values=expected_feature_list_output)
