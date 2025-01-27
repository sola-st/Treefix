# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    example(features=features({
        "a": float_feature([1]),
    })),
    example(features=features({}))
]

serialized = [m.SerializeToString() for m in original]

expected_output = {
    "a":
        np.array([[1], [-1]], dtype=np.float32)  # 2x1 (column vector)
}

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "a":
                parsing_ops.FixedLenFeature(
                    (1,), dtype=dtypes.float32, default_value=-1),
        }
    }, expected_output)
