# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_d9m_test.py
op_should_throw_for_float = {
    math_ops.unsorted_segment_max: False,
    math_ops.unsorted_segment_min: False,
    math_ops.unsorted_segment_mean: True,  # uses unsorted_segment_sum
    math_ops.unsorted_segment_sqrt_n: True,  # uses unsorted_segment_sum
    math_ops.unsorted_segment_prod: True,
    math_ops.unsorted_segment_sum: True,
}
with self.session(force_gpu=True):
    for op, should_throw_for_float in op_should_throw_for_float.items():
        for segment_ids_type in [dtypes.int32, dtypes.int64]:
            for data_type in [
                dtypes.float16, dtypes.float32, dtypes.float64, dtypes.int32
            ]:
                if (op == math_ops.unsorted_segment_sqrt_n and
                    data_type == dtypes.int32):  # sqrt_n doesn't support int32
                    continue
                data, segment_ids, num_segments = self._input(
                    data_type, segment_ids_type)
                result = op(data, segment_ids, num_segments)
                self.evaluate(result)
