# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
expected_st_a = (  # indices, values, shape
    np.empty((0, 2), dtype=np.int64),  # indices
    np.empty((0,), dtype=np.int64),  # sp_a is DT_INT64
    np.array([2, 0], dtype=np.int64))  # batch == 2, max_elems = 0
expected_sp = (  # indices, values, shape
    np.array([[0, 0], [0, 3], [1, 7]],
             dtype=np.int64), np.array(["a", "b", "c"], dtype="|S"),
    np.array([2, 13], dtype=np.int64))  # batch == 4, max_elems = 13

original = [
    example(
        features=features({
            "c": float_feature([3, 4]),
            "val": bytes_feature([b"a", b"b"]),
            "idx": int64_feature([0, 3])
        })),
    example(
        features=features({
            "c": float_feature([1, 2]),
            "val": bytes_feature([b"c"]),
            "idx": int64_feature([7])
        }))
]

names = ["in1", "in2"]
serialized = [m.SerializeToString() for m in original]

a_default = [1, 2, 3]
b_default = np.random.rand(3, 3).astype(bytes)
expected_output = {
    "st_a": expected_st_a,
    "sp": expected_sp,
    "a": np.array(2 * [[a_default]]),
    "b": np.array(2 * [b_default]),
    "c": np.array([[3, 4], [1, 2]], dtype=np.float32),
}

self._test(
    {
        "example_names": names,
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "st_a":
                parsing_ops.VarLenFeature(dtypes.int64),
            "sp":
                parsing_ops.SparseFeature("idx", "val", dtypes.string, 13),
            "a":
                parsing_ops.FixedLenFeature(
                    (1, 3), dtypes.int64, default_value=a_default),
            "b":
                parsing_ops.FixedLenFeature(
                    (3, 3), dtypes.string, default_value=b_default),
            # Feature "c" must be provided, since it has no default_value.
            "c":
                parsing_ops.FixedLenFeature((2,), dtypes.float32),
        }
    },
    expected_output)
