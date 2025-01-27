# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = sequence_example(
    feature_lists=feature_lists({
        "st_a":
            feature_list([
                float_feature([3.0, 4.0]),
                feature(),
                float_feature([5.0]),
            ]),
    }))

serialized = original.SerializeToString()

expected_st_a = (
    np.array([[0, 0], [0, 1], [2, 0]], dtype=np.int64),  # indices
    np.array([3.0, 4.0, 5.0], dtype=np.float32),  # values
    np.array([3, 2], dtype=np.int64))  # shape: num_time = 3, max_feat = 2

expected_feature_list_output = {
    "st_a": expected_st_a,
}

self._testBoth(
    {
        "example_name": "in1",
        "serialized": ops.convert_to_tensor(serialized),
        "sequence_features": {
            "st_a": parsing_ops.VarLenFeature(dtypes.float32),
        }
    },
    expected_feat_list_values=expected_feature_list_output)
