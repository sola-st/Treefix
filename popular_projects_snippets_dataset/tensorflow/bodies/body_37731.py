# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    example(
        features=features({
            "val": float_feature([3, 4]),
            "idx0": int64_feature([5, 10]),
            "idx1": int64_feature([0, 2]),
        })),
    example(
        features=features({
            "val": float_feature([]),  # empty float list
            "idx0": int64_feature([]),
            "idx1": int64_feature([]),
        })),
    example(
        features=features({
            "val": feature(),  # feature with nothing in it
            # missing idx feature
        })),
    example(
        features=features({
            "val": float_feature([1, 2, -1]),
            "idx0": int64_feature([0, 9, 3]),  # unsorted
            "idx1": int64_feature([1, 0, 2]),
        }))
]

serialized = [m.SerializeToString() for m in original]

expected_sp = (
    # indices
    np.array([[0, 5, 0], [0, 10, 2], [3, 0, 1], [3, 3, 2], [3, 9, 0]],
             dtype=np.int64),
    # values
    np.array([3.0, 4.0, 1.0, -1.0, 2.0], dtype=np.float32),
    # shape batch == 4, max_elems = 13
    np.array([4, 13, 3], dtype=np.int64))

expected_output = {
    "sp": expected_sp,
}

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "sp":
                parsing_ops.SparseFeature(["idx0", "idx1"], "val",
                                          dtypes.float32, [13, 3])
        }
    }, expected_output)
