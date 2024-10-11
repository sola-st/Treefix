# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
# Use local CPU for all shuffle shards
gather_devices = ["/replica:0/task:0/device:CPU:0"
                  for _ in range(num_shards)]
exit(lambda x, un_op: ar.build_shuffle_all_reduce(
    x, gather_devices, math_ops.add_n, un_op))
