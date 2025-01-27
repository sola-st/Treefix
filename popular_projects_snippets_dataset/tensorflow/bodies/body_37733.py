# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
aname = "a"
bname = "b*has+a:tricky_name"
# TODO(lew): Feature appearing twice should be an error in future.
original = [
    (example(features=features({
        aname: float_feature([10, 10]),
    })),
     example(
         features=features({
             aname: float_feature([1, 1]),
             bname: bytes_feature([b"b0_str"]),
         }))),
    (
        example(features=features({
            bname: bytes_feature([b"b100"]),
        })),
        example(
            features=features({
                aname: float_feature([-1, -1]),
                bname: bytes_feature([b"b1"]),
            })),
    ),
]

serialized = [
    m.SerializeToString() + n.SerializeToString() for (m, n) in original
]

# pylint: disable=too-many-function-args
expected_output = {
    aname:
        np.array([[1, 1], [-1, -1]], dtype=np.float32).reshape(2, 1, 2, 1),
    bname:
        np.array(["b0_str", "b1"], dtype=bytes).reshape(2, 1, 1, 1, 1),
}
# pylint: enable=too-many-function-args

# No defaults, values required
self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            aname:
                parsing_ops.FixedLenFeature(
                    (1, 2, 1), dtype=dtypes.float32),
            bname:
                parsing_ops.FixedLenFeature(
                    (1, 1, 1, 1), dtype=dtypes.string),
        }
    }, expected_output)
