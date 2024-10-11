# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = [
    example(features=features({
        "val": float_feature([3, 4]),
        "idx": int64_feature([5, 10])
    })),
    example(features=features({
        "val": float_feature([]),  # empty float list
        "idx": int64_feature([])
    })),
    example(features=features({
        "val": feature(),  # feature with nothing in it
        # missing idx feature
    })),
    example(features=features({
        "val": float_feature([1, 2, -1]),
        "idx":
            int64_feature([0, 9, 3])  # unsorted
    }))
]

expected_outputs = [{
    "sp": (np.array([[5], [10]], dtype=np.int64),
           np.array([3.0, 4.0], dtype=np.float32),
           np.array([13], dtype=np.int64))
}, {
    "sp": empty_sparse(np.float32, shape=[13])
}, {
    "sp": empty_sparse(np.float32, shape=[13])
}, {
    "sp": (np.array([[0], [3], [9]], dtype=np.int64),
           np.array([1.0, -1.0, 2.0], dtype=np.float32),
           np.array([13], dtype=np.int64))
}]

for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            "sp":
                parsing_ops.SparseFeature(["idx"], "val", dtypes.float32,
                                          [13])
        }
    }, expected_output)
