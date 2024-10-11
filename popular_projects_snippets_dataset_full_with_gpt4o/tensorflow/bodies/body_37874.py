# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = example(features=features({
    "c": float_feature([3, 4]),
    "d": float_feature([0.0, 1.0]),
    "val": bytes_feature([b"a", b"b"]),
    "idx": int64_feature([0, 3]),
    "st_a": float_feature([3.0, 4.0])
}))

serialized = original.SerializeToString()

expected_st_a = (
    np.array(
        [[0], [1]], dtype=np.int64),  # indices
    np.array(
        [3.0, 4.0], dtype=np.float32),  # values
    np.array(
        [2], dtype=np.int64))  # shape: max_values = 2

expected_sp = (  # indices, values, shape
    np.array(
        [[0], [3]], dtype=np.int64), np.array(
            ["a", "b"], dtype="|S"), np.array(
                [13], dtype=np.int64))  # max_values = 13

a_default = [1, 2, 3]
b_default = np.random.rand(3, 3).astype(bytes)
expected_output = {
    "st_a": expected_st_a,
    "sp": expected_sp,
    "a": [a_default],
    "b": b_default,
    "c": np.array([3, 4], dtype=np.float32),
    "d": np.array([0.0, 1.0], dtype=np.float32),
}

self._test(
    {
        "serialized":
            ops.convert_to_tensor(serialized),
        "features": {
            "st_a":
                parsing_ops.VarLenFeature(dtypes.float32),
            "sp":
                parsing_ops.SparseFeature(
                    ["idx"], "val", dtypes.string, [13]),
            "a":
                parsing_ops.FixedLenFeature(
                    (1, 3), dtypes.int64, default_value=a_default),
            "b":
                parsing_ops.FixedLenFeature(
                    (3, 3), dtypes.string, default_value=b_default),
            # Feature "c" must be provided, since it has no default_value.
            "c":
                parsing_ops.FixedLenFeature(2, dtypes.float32),
            "d":
                parsing_ops.FixedLenSequenceFeature([],
                                                    dtypes.float32,
                                                    allow_missing=True)
        }
    },
    expected_output)
