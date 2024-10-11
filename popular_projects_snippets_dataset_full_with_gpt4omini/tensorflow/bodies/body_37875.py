# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
serialized = example(
    features=features({
        "a": bytes_feature([b"a", b"b"]),
    })).SerializeToString()
self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "a": parsing_ops.FixedLenFeature(1, dtypes.string)
        }
    },
    expected_err=(errors_impl.OpError, "Can't parse serialized Example"))
