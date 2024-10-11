# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
expected_idx = (  # indices, values, shape
    np.array([[0, 0], [0, 1], [1, 0], [1, 1]],
             dtype=np.int64), np.array([0, 3, 7, 1]),
    np.array([2, 2], dtype=np.int64))  # batch == 4, max_elems = 2

expected_sp = (  # indices, values, shape
    np.array([[0, 0], [0, 3], [1, 1], [1, 7]],
             dtype=np.int64), np.array(["a", "b", "d", "c"], dtype="|S"),
    np.array([2, 13], dtype=np.int64))  # batch == 4, max_elems = 13

original = [
    example(
        features=features({
            "val": bytes_feature([b"a", b"b"]),
            "idx": int64_feature([0, 3])
        })),
    example(
        features=features({
            "val": bytes_feature([b"c", b"d"]),
            "idx": int64_feature([7, 1])
        }))
]

names = ["in1", "in2"]
serialized = [m.SerializeToString() for m in original]

expected_output = {
    "idx": expected_idx,
    "sp": expected_sp,
}

self._test(
    {
        "example_names": names,
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "idx":
                parsing_ops.VarLenFeature(dtypes.int64),
            "sp":
                parsing_ops.SparseFeature(["idx"], "val", dtypes.string,
                                          [13]),
        }
    }, expected_output)
