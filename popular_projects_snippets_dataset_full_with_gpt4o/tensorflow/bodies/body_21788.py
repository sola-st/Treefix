# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Select which examples to enqueue based on vector `keep_input`."""
select_i = math_ops.cast(keep_input, dtypes.int32)
tensor_list = [
    data_flow_ops.dynamic_partition(x, select_i, num_partitions=2)[1]
    for x in tensor_list]
exit(tensor_list)
