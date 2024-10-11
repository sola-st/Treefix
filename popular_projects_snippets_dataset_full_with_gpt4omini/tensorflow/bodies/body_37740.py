# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
aname = "a"
bname = "b"
cname = "c"
dname = "d"
example_names = ["in1", "in2", "in3", "in4"]
original = [
    example(features=features({
        cname: int64_feature([2]),
    })),
    example(
        features=features({
            aname: float_feature([1, 1]),
            bname: bytes_feature([b"b0_str", b"b1_str"]),
        })),
    example(
        features=features({
            aname: float_feature([-1, -1, 2, 2]),
            bname: bytes_feature([b"b1"]),
        })),
    example(
        features=features({
            aname: float_feature([]),
            cname: int64_feature([3]),
        })),
]

serialized = [m.SerializeToString() for m in original]

# pylint: disable=too-many-function-args
expected_output = {
    aname:
        np.array(
            [
                [0, 0, 0, 0],
                [1, 1, 0, 0],
                [-1, -1, 2, 2],
                [0, 0, 0, 0],
            ],
            dtype=np.float32).reshape(4, 2, 2, 1),
    bname:
        np.array(
            [["", ""], ["b0_str", "b1_str"], ["b1", ""], ["", ""]],
            dtype=bytes).reshape(4, 2, 1, 1, 1),
    cname:
        np.array([2, 0, 0, 3], dtype=np.int64).reshape(4, 1),
    dname:
        np.empty(shape=(4, 0), dtype=bytes),
}
# pylint: enable=too-many-function-args

self._test(
    {
        "example_names": example_names,
        "serialized": ops.convert_to_tensor(serialized),
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
expected_output_custom_padding = dict(expected_output)
# pylint: disable=too-many-function-args
expected_output_custom_padding[aname] = np.array(
    [
        [-2, -2, -2, -2],
        [1, 1, -2, -2],
        [-1, -1, 2, 2],
        [-2, -2, -2, -2],
    ],
    dtype=np.float32).reshape(4, 2, 2, 1)
# pylint: enable=too-many-function-args

self._test(
    {
        "example_names": example_names,
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            aname:
                parsing_ops.FixedLenSequenceFeature((2, 1),
                                                    dtype=dtypes.float32,
                                                    allow_missing=True,
                                                    default_value=-2.0),
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
    }, expected_output_custom_padding)

# Change number of required values so the inputs are not a
# multiple of this size.
self._test(
    {
        "example_names": example_names,
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            aname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1), dtype=dtypes.float32, allow_missing=True),
            bname:
                parsing_ops.FixedLenSequenceFeature(
                    (2, 1, 1), dtype=dtypes.string, allow_missing=True),
        }
    },
    expected_err=(
        errors_impl.OpError, "Name: in3, Key: b, Index: 2.  "
        "Number of bytes values is not a multiple of stride length."))

self._test(
    {
        "example_names": example_names,
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            aname:
                parsing_ops.FixedLenSequenceFeature((2, 1),
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
        "example_names": example_names,
        "serialized": ops.convert_to_tensor(serialized),
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
        "example_names": example_names,
        "serialized": ops.convert_to_tensor(serialized),
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
        "example_names": example_names,
        "serialized": ops.convert_to_tensor(serialized),
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
