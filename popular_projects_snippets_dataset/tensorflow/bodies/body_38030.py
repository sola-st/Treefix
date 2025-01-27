# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_d9m_test.py
dtypes_to_test = [dtypes.float16, dtypes.float32, dtypes.float64]
if not test.is_built_with_rocm():
    dtypes_to_test += [dtypes.complex64, dtypes.complex128]
for data_type in dtypes_to_test:
    for segment_ids_type in [dtypes.int32, dtypes.int64]:
        with self.cached_session(force_gpu=True):
            params, indices, _ = self._input(data_type, segment_ids_type)
            params = variables.Variable(params)
            with backprop.GradientTape() as tape:
                tape.watch(params)
                op_output = array_ops.gather(params, indices)
            gradient = tape.gradient(op_output, params)
            self.evaluate(params.assign(gradient))
