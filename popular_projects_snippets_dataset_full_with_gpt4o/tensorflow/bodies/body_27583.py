# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
aname = "a"
bname = "b"
cname = "c"
original = [
    example(features=features({
        cname: int64_feature([2]),
    })),
    example(features=features({
        aname: float_feature([1, 1]),
        bname: bytes_feature([b"b0_str", b"b1_str"]),
    })),
    example(features=features({
        aname: float_feature([-1, -1, 2, 2]),
        bname: bytes_feature([b"b1"]),
    })),
    example(features=features({
        aname: float_feature([]),
        cname: int64_feature([3]),
    })),
]

serialized = [m.SerializeToString() for m in original]
if context.executing_eagerly():
    self._test(
        ops.convert_to_tensor(serialized), {
            aname:
                parsing_ops.FixedLenSequenceFeature((2, 1),
                                                    dtype=dtypes.float32,
                                                    allow_missing=True,
                                                    default_value=[]),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1, 1), dtype=dtypes.string, allow_missing=True),
        },
        expected_err=(errors_impl.InvalidArgumentError,
                      "Input to reshape is a tensor with 0 values"))
else:
    self._test(
        ops.convert_to_tensor(serialized), {
            aname:
                parsing_ops.FixedLenSequenceFeature((2, 1),
                                                    dtype=dtypes.float32,
                                                    allow_missing=True,
                                                    default_value=[]),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1, 1), dtype=dtypes.string, allow_missing=True),
        },
        expected_err=(ValueError,
                      "Cannot reshape a tensor with 0 elements to shape"))
