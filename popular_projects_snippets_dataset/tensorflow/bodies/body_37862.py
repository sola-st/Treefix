# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
original = [
    example(features=features({
        "st_c": float_feature([3, 4])
    })),
    example(features=features({
        "st_c": float_feature([]),  # empty float list
    })),
    example(features=features({
        "st_d": feature(),  # feature with nothing in it
    })),
    example(features=features({
        "st_c": float_feature([1, 2, -1]),
        "st_d": bytes_feature([b"hi"])
    }))
]

expected_outputs = [{
    "st_c": (np.array([[0], [1]], dtype=np.int64),
             np.array([3.0, 4.0], dtype=np.float32),
             np.array([2], dtype=np.int64)),
    "st_d":
        empty_sparse(bytes)
}, {
    "st_c": empty_sparse(np.float32),
    "st_d": empty_sparse(bytes)
}, {
    "st_c": empty_sparse(np.float32),
    "st_d": empty_sparse(bytes)
}, {
    "st_c": (np.array([[0], [1], [2]], dtype=np.int64),
             np.array([1.0, 2.0, -1.0], dtype=np.float32),
             np.array([3], dtype=np.int64)),
    "st_d": (np.array([[0]], dtype=np.int64), np.array(["hi"], dtype=bytes),
             np.array([1], dtype=np.int64))
}]

for proto, expected_output in zip(original, expected_outputs):
    self._test({
        "serialized": ops.convert_to_tensor(proto.SerializeToString()),
        "features": {
            "st_c": parsing_ops.VarLenFeature(dtypes.float32),
            "st_d": parsing_ops.VarLenFeature(dtypes.string)
        },
    }, expected_output)
