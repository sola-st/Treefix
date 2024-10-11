# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
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

serialized = [m.SerializeToString() for m in original]

expected_output = {
    aname:
        np.array(  # pylint: disable=too-many-function-args
            [[1, 1], [-1, -1]],
            dtype=np.float32).reshape(2, 1, 2, 1),
    bname:
        np.array(  # pylint: disable=too-many-function-args
            ["b0_str", ""],
            dtype=bytes).reshape(2, 1, 1, 1, 1),
}

# No defaults, values required
self._test(
    ops.convert_to_tensor(serialized), {
        aname:
            parsing_ops.FixedLenFeature((1, 2, 1), dtype=dtypes.float32),
        bname:
            parsing_ops.FixedLenFeature((1, 1, 1, 1), dtype=dtypes.string),
    },
    expected_values=expected_output,
    create_iterator_twice=True)
