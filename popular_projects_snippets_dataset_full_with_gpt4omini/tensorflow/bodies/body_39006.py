# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
with self.cached_session(use_gpu=False) as sess:
    sp_input = self._SparseTensorValue_5x6(np.arange(6))
    serialized = serialize_fn(sp_input, out_type=out_type)
    sp_deserialized = deserialize_fn(serialized, dtype=dtypes.int32)

    indices, values, shape = self.evaluate(sp_deserialized)

    self.assertAllEqual(indices, sp_input[0])
    self.assertAllEqual(values, sp_input[1])
    self.assertAllEqual(shape, sp_input[2])
