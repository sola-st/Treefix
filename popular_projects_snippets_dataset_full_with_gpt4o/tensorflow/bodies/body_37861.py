# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = example(features=features({
    "a": float_feature([1, 1, 3]),
}))

serialized = original.SerializeToString()

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "a": parsing_ops.FixedLenFeature(None, dtypes.float32)
        }
    },
    expected_err=(ValueError, "Missing shape for feature a"))
