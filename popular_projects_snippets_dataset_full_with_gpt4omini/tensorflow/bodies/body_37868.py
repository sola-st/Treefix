# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = [
    example(features=features({
        "a": float_feature([1]),
    })), example(features=features({}))
]

expected_outputs = [{
    "a": np.array([1], dtype=np.float32)
}, {
    "a": np.array([-1], dtype=np.float32)
}]

for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            "a":
                parsing_ops.FixedLenFeature(
                    (1,), dtype=dtypes.float32, default_value=-1),
        }
    }, expected_output)
