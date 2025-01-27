# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = [
    example(features=features({
        "c": float_feature([3, 4]),
        "val": bytes_feature([b"a", b"b"]),
        "idx": int64_feature([0, 3])
    })), example(features=features({
        "c": float_feature([1, 2]),
        "val": bytes_feature([b"c"]),
        "idx": int64_feature([7])
    }))
]

a_default = np.array([[1, 2, 3]], dtype=np.int64)
b_default = np.random.rand(3, 3).astype(bytes)

expected_st_a = empty_sparse(np.int64)

expected_outputs = [{
    "st_a":
        expected_st_a,
    "sp": (np.array([[0], [3]], dtype=np.int64),
           np.array(["a", "b"], dtype=bytes), np.array(
               [13], dtype=np.int64)),
    "a":
        a_default,
    "b":
        b_default,
    "c":
        np.array([3, 4], dtype=np.float32)
}, {
    "st_a":
        expected_st_a,
    "sp": (np.array([[7]], dtype=np.int64), np.array(["c"], dtype=bytes),
           np.array([13], dtype=np.int64)),
    "a":
        a_default,
    "b":
        b_default,
    "c":
        np.array([1, 2], dtype=np.float32)
}]

for proto, expected_output in zip(original, expected_outputs):
    self._test(
        {
            "serialized": ops.convert_to_tensor(proto.SerializeToString()),
            "features": {
                "st_a":
                    parsing_ops.VarLenFeature(dtypes.int64),
                "sp":
                    parsing_ops.SparseFeature("idx", "val", dtypes.string, 13
                                             ),
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
