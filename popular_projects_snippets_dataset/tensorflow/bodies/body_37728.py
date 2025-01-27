# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    example(features=features({"st_c": float_feature([3, 4])})),
    example(
        features=features({
            "st_c": float_feature([]),  # empty float list
        })),
    example(
        features=features({
            "st_d": feature(),  # feature with nothing in it
        })),
    example(
        features=features({
            "st_c": float_feature([1, 2, -1]),
            "st_d": bytes_feature([b"hi"])
        }))
]

serialized = [m.SerializeToString() for m in original]

expected_st_c = (  # indices, values, shape
    np.array([[0, 0], [0, 1], [3, 0], [3, 1], [3, 2]], dtype=np.int64),
    np.array([3.0, 4.0, 1.0, 2.0, -1.0], dtype=np.float32),
    np.array([4, 3], dtype=np.int64))  # batch == 2, max_elems = 3

expected_st_d = (  # indices, values, shape
    np.array([[3, 0]], dtype=np.int64), np.array(["hi"], dtype=bytes),
    np.array([4, 1], dtype=np.int64))  # batch == 2, max_elems = 1

expected_output = {
    "st_c": expected_st_c,
    "st_d": expected_st_d,
}

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": {
            "st_c": parsing_ops.VarLenFeature(dtypes.float32),
            "st_d": parsing_ops.VarLenFeature(dtypes.string)
        }
    }, expected_output)
