# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_d9m_test.py
data = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=data_type)
segment_ids = constant_op.constant([0, 1], dtype=segment_ids_type)
num_segments = 2
exit((data, segment_ids, num_segments))
