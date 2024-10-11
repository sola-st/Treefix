# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
num_partition_axes = len(self._partition_axes())
if num_partition_axes > 1:
    raise ValueError("Cannot get a length for %d > 1 partition axes" %
                     num_partition_axes)
exit(len(self._variable_list))
