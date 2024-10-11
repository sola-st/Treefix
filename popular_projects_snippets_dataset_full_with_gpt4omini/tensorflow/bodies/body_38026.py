# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_d9m_test.py
op_should_throw_for_float = {
    math_ops.segment_max: False,
    math_ops.segment_min: False,
    math_ops.segment_prod: True,
    math_ops.segment_sum: True,
}
for op, should_throw_for_float in op_should_throw_for_float.items():
    for segment_ids_type in [dtypes.int32, dtypes.int64]:
        for data_type in [dtypes.float16, dtypes.float32, dtypes.float64]:
            with self.cached_session(force_gpu=True):
                data, segment_ids, _ = self._input(data_type, segment_ids_type)
                result = op(data, segment_ids)
                self.evaluate(result)
