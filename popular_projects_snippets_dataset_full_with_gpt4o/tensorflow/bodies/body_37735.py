# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    example(features=features({
        "a": float_feature([1, 1]),
    })),
    example(features=features({
        "b": bytes_feature([b"b1"]),
    })),
    example(features=features({"b": feature()})),
]

serialized = [m.SerializeToString() for m in original]

# pylint: disable=too-many-function-args
expected_output = {
    "a":
        np.array(
            [[1, 1], [3, -3], [3, -3]],
            dtype=np.float32).reshape(3, 1, 2, 1),
    "b":
        np.array(
            ["tmp_str", "b1", "tmp_str"],
            dtype=bytes).reshape(3, 1, 1, 1, 1),
}
# pylint: enable=too-many-function-args

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "a":
                parsing_ops.FixedLenFeature((1, 2, 1),
                                            dtype=dtypes.float32,
                                            default_value=[3.0, -3.0]),
            "b":
                parsing_ops.FixedLenFeature((1, 1, 1, 1),
                                            dtype=dtypes.string,
                                            default_value="tmp_str"),
        }
    }, expected_output)
