# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_d9m_test.py
with self.session(force_gpu=True):
    dtypes_to_test = [dtypes.float16, dtypes.float32, dtypes.float64]
    if not test.is_built_with_rocm():
        dtypes_to_test += [dtypes.complex64, dtypes.complex128]
    for data_type in dtypes_to_test:
        for segment_ids_type in [dtypes.int32, dtypes.int64]:
            values, indices, _ = self._input(data_type, segment_ids_type)
            sparse_value = indexed_slices.IndexedSlices(
                values, indices, dense_shape=values.shape)
            result = ops.convert_to_tensor(sparse_value)
            self.evaluate(result)
