# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
data_i = array_ops.gather(data, i)
data_0 = array_ops.gather(data, 0)
indices_i = array_ops.gather(indices, i)
indices_0 = array_ops.gather(indices, 0)
seg_ids_i = array_ops.gather(seg_ids, i)
seg_ids_0 = array_ops.gather(seg_ids, 0)
outputs = [
    op_func(data_0, indices_i, seg_ids_0, num_segments=num_segments),
    op_func(data_i, indices_i, seg_ids_0, num_segments=num_segments),
    op_func(data_0, indices_0, seg_ids_0, num_segments=num_segments),
    op_func(data_i, indices_0, seg_ids_0, num_segments=num_segments)
]
if with_num_segments:
    # For this case, we support loop variant segment_ids as well.
    outputs += [
        op_func(data_0, indices_i, seg_ids_i, num_segments=num_segments),
        op_func(data_i, indices_i, seg_ids_i, num_segments=num_segments),
        op_func(data_0, indices_0, seg_ids_i, num_segments=num_segments),
        op_func(data_i, indices_0, seg_ids_i, num_segments=num_segments)
    ]
exit(outputs)
