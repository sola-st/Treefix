# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = [
    example(features=features({
        "val": float_feature([3, 4]),
        "idx0": int64_feature([5, 10]),
        "idx1": int64_feature([0, 2]),
    })),
    example(features=features({
        "val": float_feature([]),  # empty float list
        "idx0": int64_feature([]),
        "idx1": int64_feature([]),
    })),
    example(features=features({
        "val": feature(),  # feature with nothing in it
        # missing idx feature
    })),
    example(features=features({
        "val": float_feature([1, 2, -1]),
        "idx0": int64_feature([0, 9, 3]),  # unsorted
        "idx1": int64_feature([1, 0, 2]),
    }))
]

expected_outputs = [{
    "sp": (np.array([[5, 0], [10, 2]], dtype=np.int64),
           np.array([3.0, 4.0], dtype=np.float32),
           np.array([13, 3], dtype=np.int64))
}, {
    "sp": empty_sparse(np.float32, shape=[13, 3])
}, {
    "sp": empty_sparse(np.float32, shape=[13, 3])
}, {
    "sp": (np.array([[0, 1], [3, 2], [9, 0]], dtype=np.int64),
           np.array([1.0, -1.0, 2.0], dtype=np.float32),
           np.array([13, 3], dtype=np.int64))
}]

for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            "sp":
                parsing_ops.SparseFeature(["idx0", "idx1"], "val",
                                          dtypes.float32, [13, 3])
        }
    }, expected_output)
