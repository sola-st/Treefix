# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = example(features=features({
    "a": float_feature([-1, -1]),
}))

serialized = original.SerializeToString()

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "a": parsing_ops.FixedLenFeature((1, 3), dtypes.float32)
        }
    },
    # TODO(mrry): Consider matching the `io.parse_example()` error message.
    expected_err=(errors_impl.OpError, "Key: a."))
