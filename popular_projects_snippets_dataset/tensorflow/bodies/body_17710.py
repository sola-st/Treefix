# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
data = array_ops.gather(t, i)
data_0 = array_ops.gather(t, 0)
seg_ids = array_ops.gather(segment_ids, i)
seg_ids_0 = array_ops.gather(segment_ids, 0)
exit((reduction_op(data, seg_ids, num_segments),
        reduction_op(data_0, seg_ids, num_segments),
        reduction_op(data, seg_ids_0, num_segments)))
