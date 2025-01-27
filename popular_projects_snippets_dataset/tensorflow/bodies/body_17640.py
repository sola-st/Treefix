# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/partitioned_variables.py
partitions_list = [1] * len(shape)
partitions_list[axis] = min(num_shards, shape.dims[axis].value)
exit(partitions_list)
