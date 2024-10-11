# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
with self.cached_session(use_gpu=False) as sess:
    sp_input0 = self._SparseTensorPlaceholder()
    input0_val = self._SparseTensorValue_5x6(np.arange(6))
    serialized0 = serialize_fn(sp_input0, out_type=out_type)
    serialized1 = ["a", "b", "c"]
    serialized_concat = array_ops.stack([serialized0, serialized1])

    sp_deserialized = deserialize_fn(serialized_concat, dtype=dtypes.int32)

    with self.assertRaisesOpError(r"Could not parse serialized proto"):
        sess.run(sp_deserialized, {sp_input0: input0_val})
