# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    example(
        features=features({
            "val": float_feature([3, 4]),
            "idx": int64_feature([5, 10])
        })),
    example(
        features=features({
            "val": float_feature([]),  # empty float list
            "idx": int64_feature([])
        })),
    example(
        features=features({
            "val": feature(),  # feature with nothing in it
            # missing idx feature
        })),
    example(
        features=features({
            "val": float_feature([1, 2, -1]),
            "idx":
                int64_feature([0, 9, 3])  # unsorted
        }))
]

serialized = [m.SerializeToString() for m in original]

expected_sp = (  # indices, values, shape
    np.array([[0, 5], [0, 10], [3, 0], [3, 3], [3, 9]], dtype=np.int64),
    np.array([3.0, 4.0, 1.0, -1.0, 2.0], dtype=np.float32),
    np.array([4, 13], dtype=np.int64))  # batch == 4, max_elems = 13

expected_output = {
    "sp": expected_sp,
}

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "sp":
                parsing_ops.SparseFeature(["idx"], "val", dtypes.float32,
                                          [13])
        }
    }, expected_output)
