# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = [
    example(features=features({"rt_c": float_feature([3, 4])})),
    example(
        features=features({
            "rt_c": float_feature([]),  # empty float list
        })),
    example(
        features=features({
            "rt_d": feature(),  # feature with nothing in it
        })),
    example(
        features=features({
            "rt_c": float_feature([1, 2, -1]),
            "rt_d": bytes_feature([b"hi"])
        }))
]
serialized = [m.SerializeToString() for m in original]

test_features = {
    "rt_c":
        parsing_ops.RaggedFeature(dtype=dtypes.float32),
    "rt_d":
        parsing_ops.RaggedFeature(
            dtype=dtypes.string, row_splits_dtype=dtypes.int64)
}

expected_rt_c = ragged_factory_ops.constant(
    [[3.0, 4.0], [], [], [1.0, 2.0, -1.0]],
    dtype=dtypes.float32,
    row_splits_dtype=dtypes.int32)
expected_rt_d = ragged_factory_ops.constant([[], [], [], [b"hi"]])

expected_output = {
    "rt_c": expected_rt_c,
    "rt_d": expected_rt_d,
}

self._test(
    {
        "serialized": ops.convert_to_tensor(serialized),
        "features": test_features
    }, expected_output)

# Test with a large enough batch to ensure that the minibatch size is >1.
batch_serialized = serialized * 64
self.assertEqual(expected_rt_c.row_splits.dtype, np.int32)
batch_expected_out = {
    "rt_c": ragged_concat_ops.concat([expected_rt_c] * 64, axis=0),
    "rt_d": ragged_concat_ops.concat([expected_rt_d] * 64, axis=0)
}
self.assertEqual(batch_expected_out["rt_c"].row_splits.dtype, dtypes.int32)
self._test(
    {
        "serialized": ops.convert_to_tensor(batch_serialized),
        "features": test_features
    }, batch_expected_out)
