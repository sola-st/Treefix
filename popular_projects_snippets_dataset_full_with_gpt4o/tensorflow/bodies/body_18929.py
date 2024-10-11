# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/compiled_collective_ops_gpu_test.py
exit(collective_ops.all_reduce_v2(
    t=v,
    group_size=2,
    group_key=1,
    instance_key=1,
    merge_op='Add',
    final_op='Id'))
