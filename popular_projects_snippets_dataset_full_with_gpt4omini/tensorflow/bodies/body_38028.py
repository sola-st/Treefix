# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_d9m_test.py
for op in [
    math_ops.unsorted_segment_sum,
]:
    for data_type in [dtypes.complex64, dtypes.complex128]:
        for segment_ids_type in [dtypes.int32, dtypes.int64]:
            with self.cached_session(force_gpu=True):
                data, segment_ids, num_segments = self._input(
                    data_type, segment_ids_type)
                result = op(data, segment_ids, num_segments)
                self.evaluate(result)
