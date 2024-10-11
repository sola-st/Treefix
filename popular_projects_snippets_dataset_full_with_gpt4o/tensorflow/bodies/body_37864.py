# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = [
    example(features=features({
        "val1": float_feature([3, 4]),
        "val2": float_feature([5, 6]),
        "idx": int64_feature([5, 10])
    })),
    example(features=features({
        "val1": float_feature([]),  # empty float list
        "idx": int64_feature([])
    })),
]

expected_outputs = [{
    "sp1": (np.array([[5], [10]], dtype=np.int64),
            np.array([3.0, 4.0], dtype=np.float32),
            np.array([13], dtype=np.int64)),
    "sp2": (np.array([[5], [10]], dtype=np.int64),
            np.array([5.0, 6.0], dtype=np.float32),
            np.array([7], dtype=np.int64))
}, {
    "sp1": empty_sparse(np.float32, shape=[13]),
    "sp2": empty_sparse(np.float32, shape=[7])
}]

for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            "sp1":
                parsing_ops.SparseFeature("idx", "val1", dtypes.float32, 13),
            "sp2":
                parsing_ops.SparseFeature(
                    "idx",
                    "val2",
                    dtypes.float32,
                    size=7,
                    already_sorted=True)
        }
    }, expected_output)
