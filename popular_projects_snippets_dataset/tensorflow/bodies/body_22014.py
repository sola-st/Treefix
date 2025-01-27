# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
# Partition each var into 2 equal slices.
partitions = [1] * len(shape)
partitions[0] = min(2, shape.dims[0].value)
exit(partitions)
