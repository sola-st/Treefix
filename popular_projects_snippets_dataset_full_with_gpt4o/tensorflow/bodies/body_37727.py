# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    example(features=features({
        "a": float_feature([1, 1, 3]),
    })),
]

serialized = [m.SerializeToString() for m in original]

self._test(
    {
        "example_names": ["failing"],
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "a": parsing_ops.FixedLenFeature(None, dtypes.float32)
        }
    },
    expected_err=(ValueError, "Missing shape for feature a"))
