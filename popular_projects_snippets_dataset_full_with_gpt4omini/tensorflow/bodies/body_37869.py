# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = [
    example(features=features({
        "a": float_feature([1, 1]),
    })),
    example(features=features({
        "b": bytes_feature([b"b1"]),
    })),
    example(features=features({
        "b": feature()
    })),
]

# pylint: disable=too-many-function-args
expected_outputs = [
    {
        "a":
            np.array([1, 1], dtype=np.float32).reshape(1, 2, 1),
        "b":
            np.array("tmp_str", dtype=bytes).reshape(
                1, 1, 1, 1)
    },
    {
        "a":
            np.array([3, -3], dtype=np.float32).reshape(1, 2, 1),
        "b":
            np.array("b1", dtype=bytes).reshape(
                1, 1, 1, 1)
    },
    {
        "a":
            np.array([3, -3], dtype=np.float32).reshape(1, 2, 1),
        "b":
            np.array("tmp_str", dtype=bytes).reshape(
                1, 1, 1, 1)
    }
]
# pylint: enable=too-many-function-args

for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            "a":
                parsing_ops.FixedLenFeature(
                    (1, 2, 1),
                    dtype=dtypes.float32,
                    default_value=[3.0, -3.0]),
            "b":
                parsing_ops.FixedLenFeature(
                    (1, 1, 1, 1),
                    dtype=dtypes.string,
                    default_value="tmp_str"),
        }
    }, expected_output)
