# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
t = random_ops.random_uniform([3, 3, 2])
for segment_ids_dtype in (dtypes.int32, dtypes.int64):
    for num_segments_dtype in (dtypes.int32, dtypes.int64):
        segment_ids = constant_op.constant([[0, 0, 2], [0, 1, 2], [2, 2, 2]],
                                           dtype=segment_ids_dtype)
        num_segments = constant_op.constant(3, dtype=num_segments_dtype)

        # pylint: disable=cell-var-from-loop
        def loop_fn(i):
            data = array_ops.gather(t, i)
            data_0 = array_ops.gather(t, 0)
            seg_ids = array_ops.gather(segment_ids, i)
            seg_ids_0 = array_ops.gather(segment_ids, 0)
            exit((reduction_op(data, seg_ids, num_segments),
                    reduction_op(data_0, seg_ids, num_segments),
                    reduction_op(data, seg_ids_0, num_segments)))

        # pylint: enable=cell-var-from-loop

        self._test_loop_fn(loop_fn, 3)
