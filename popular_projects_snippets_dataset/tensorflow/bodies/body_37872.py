# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
aname = "a"
bname = "b"
cname = "c"
dname = "d"
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

# pylint: disable=too-many-function-args
expected_outputs = [
    {
        aname: np.empty(shape=(0, 2, 1), dtype=np.int64),
        bname: np.empty(shape=(0, 1, 1, 1), dtype=bytes),
        cname: np.array([2], dtype=np.int64),
        dname: np.empty(shape=(0,), dtype=bytes)
    },
    {
        aname:
            np.array([[[1], [1]]], dtype=np.float32),
        bname:
            np.array(["b0_str", "b1_str"], dtype=bytes).reshape(2, 1, 1, 1),
        cname:
            np.empty(shape=(0,), dtype=np.int64),
        dname:
            np.empty(shape=(0,), dtype=bytes)
    },
    {
        aname: np.array([[[-1], [-1]], [[2], [2]]], dtype=np.float32),
        bname: np.array(["b1"], dtype=bytes).reshape(1, 1, 1, 1),
        cname: np.empty(shape=(0,), dtype=np.int64),
        dname: np.empty(shape=(0,), dtype=bytes)
    },
    {
        aname: np.empty(shape=(0, 2, 1), dtype=np.int64),
        bname: np.empty(shape=(0, 1, 1, 1), dtype=bytes),
        cname: np.array([3], dtype=np.int64),
        dname: np.empty(shape=(0,), dtype=bytes)
    },
]
# pylint: enable=too-many-function-args

for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            aname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1), dtype=dtypes.float32, allow_missing=True),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (1, 1, 1), dtype=dtypes.string, allow_missing=True),
            cname:
                parsing_ops.FixedLenSequenceFeature(
                    shape=[], dtype=dtypes.int64, allow_missing=True),
            dname:
                parsing_ops.FixedLenSequenceFeature(
                    shape=[], dtype=dtypes.string, allow_missing=True),
        }
    }, expected_output)

# Test with padding values.
# NOTE(mrry): Since we parse a single example at a time, the fixed-length
# sequences will not be padded, and the padding value will be ignored.
for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            aname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1), dtype=dtypes.float32, allow_missing=True),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (1, 1, 1), dtype=dtypes.string, allow_missing=True),
            cname:
                parsing_ops.FixedLenSequenceFeature(
                    shape=[], dtype=dtypes.int64, allow_missing=True),
            dname:
                parsing_ops.FixedLenSequenceFeature(
                    shape=[], dtype=dtypes.string, allow_missing=True),
        }
    }, expected_output)

# Change number of required values so the inputs are not a
# multiple of this size.
self._test(
    {
        "serialized":
            ops.convert_to_tensor(original[2].SerializeToString()),
        "features": {
            aname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1), dtype=dtypes.float32, allow_missing=True),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1, 1), dtype=dtypes.string, allow_missing=True),
        }
    },
    # TODO(mrry): Consider matching the `io.parse_example()` error message.
    expected_err=(errors_impl.OpError, "Key: b."))

self._test(
    {
        "serialized": ops.convert_to_tensor(""),
        "features": {
            aname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1),
                    dtype=dtypes.float32,
                    allow_missing=True,
                    default_value=[]),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1, 1), dtype=dtypes.string, allow_missing=True),
        }
    },
    expected_err=(ValueError,
                  "Cannot reshape a tensor with 0 elements to shape"))

self._test(
    {
        "serialized": ops.convert_to_tensor(""),
        "features": {
            aname:
                parsing_ops.FixedLenFeature(
                    (None, 2, 1), dtype=dtypes.float32),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1, 1), dtype=dtypes.string, allow_missing=True),
        }
    },
    expected_err=(ValueError,
                  "First dimension of shape for feature a unknown. "
                  "Consider using FixedLenSequenceFeature."))

self._test(
    {
        "serialized": ops.convert_to_tensor(""),
        "features": {
            cname:
                parsing_ops.FixedLenFeature(
                    (1, None), dtype=dtypes.int64, default_value=[[1]]),
        }
    },
    expected_err=(ValueError,
                  "All dimensions of shape for feature c need to be known "
                  r"but received \(1, None\)."))

self._test(
    {
        "serialized": ops.convert_to_tensor(""),
        "features": {
            aname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1), dtype=dtypes.float32, allow_missing=True),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (1, 1, 1), dtype=dtypes.string, allow_missing=True),
            cname:
                parsing_ops.FixedLenSequenceFeature(
                    shape=[], dtype=dtypes.int64, allow_missing=False),
            dname:
                parsing_ops.FixedLenSequenceFeature(
                    shape=[], dtype=dtypes.string, allow_missing=True),
        }
    },
    expected_err=(ValueError,
                  "Unsupported: FixedLenSequenceFeature requires "
                  "allow_missing to be True."))
