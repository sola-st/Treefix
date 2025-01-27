# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
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

serialized = [m.SerializeToString() for m in original]

expected_sp1 = sparse_tensor.SparseTensorValue(  # indices, values, shape
    np.array([[0, 5], [0, 10]], dtype=np.int64),
    np.array([3.0, 4.0], dtype=np.float32),
    np.array([2, 13], dtype=np.int64))  # batch == 2, max_elems = 13

expected_sp2 = sparse_tensor.SparseTensorValue(  # indices, values, shape
    np.array([[0, 5], [0, 10]], dtype=np.int64),
    np.array([5.0, 6.0], dtype=np.float32),
    np.array([2, 7], dtype=np.int64))  # batch == 2, max_elems = 13

expected_output = {
    "sp1": expected_sp1,
    "sp2": expected_sp2,
}

self._test(
    ops.convert_to_tensor(serialized), {
        "sp1":
            parsing_ops.SparseFeature("idx", "val1", dtypes.float32, 13),
        "sp2":
            parsing_ops.SparseFeature(
                "idx", "val2", dtypes.float32, size=7, already_sorted=True)
    },
    expected_values=expected_output,
    create_iterator_twice=True)
