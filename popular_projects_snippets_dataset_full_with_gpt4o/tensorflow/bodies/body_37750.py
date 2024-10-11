# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = sequence_example(
    context=features({
        "c": float_feature([3, 4]),
        "st_a": float_feature([3.0, 4.0])
    }))

serialized = original.SerializeToString()

expected_st_a = (
    np.array([[0], [1]], dtype=np.int64),  # indices
    np.array([3.0, 4.0], dtype=np.float32),  # values
    np.array([2], dtype=np.int64))  # shape: num_features = 2

a_default = [[1, 2, 3]]
b_default = np.random.rand(3, 3).astype(bytes)
expected_context_output = {
    "st_a": expected_st_a,
    "a": a_default,
    "b": b_default,
    "c": np.array([3, 4], dtype=np.float32),
}

self._testBoth(
    {
        "example_name": "in1",
        "serialized": ops.convert_to_tensor(serialized),
        "context_features": {
            "st_a":
                parsing_ops.VarLenFeature(dtypes.float32),
            "a":
                parsing_ops.FixedLenFeature(
                    (1, 3), dtypes.int64, default_value=a_default),
            "b":
                parsing_ops.FixedLenFeature(
                    (3, 3), dtypes.string, default_value=b_default),
            # Feature "c" must be provided, since it has no default_value.
            "c":
                parsing_ops.FixedLenFeature((2,), dtypes.float32),
        }
    },
    expected_context_values=expected_context_output)
