# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
aname = "a"
bname = "b*has+a:tricky_name"
original = [
    example(features=features({
        aname: float_feature([1, 1]),
        bname: bytes_feature([b"b0_str"]),
    })), example(features=features({
        aname: float_feature([-1, -1]),
        bname: bytes_feature([b""]),
    }))
]

# pylint: disable=too-many-function-args
expected_outputs = [
    {
        aname:
            np.array([1, 1], dtype=np.float32).reshape(1, 2, 1),
        bname:
            np.array(["b0_str"], dtype=bytes).reshape(
                1, 1, 1, 1)
    },
    {
        aname:
            np.array([-1, -1], dtype=np.float32).reshape(1, 2, 1),
        bname:
            np.array([""], dtype=bytes).reshape(
                1, 1, 1, 1)
    }
]
# pylint: enable=too-many-function-args

for proto, expected_output in zip(original, expected_outputs):
    # No defaults, values required
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            aname:
                parsing_ops.FixedLenFeature((1, 2, 1), dtype=dtypes.float32),
            bname:
                parsing_ops.FixedLenFeature(
                    (1, 1, 1, 1), dtype=dtypes.string),
        }
    }, expected_output)
