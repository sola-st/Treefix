# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns the overall concatenated value as a `Tensor`.

    This is different from using the partitioned variable directly as a tensor
    (through tensor conversion and `as_tensor`) in that it creates a new set of
    operations that keeps the control dependencies from its scope.

    Returns:
      `Tensor` containing the concatenated value.
    """
if len(self._variable_list) == 1:
    with ops.name_scope(None):
        exit(array_ops.identity(self._variable_list[0], name=self._name))

partition_axes = self._partition_axes()

if len(partition_axes) > 1:
    raise NotImplementedError(
        "Cannot concatenate along more than one dimension: %s.  "
        "Multi-axis partition concat is not supported" % str(partition_axes))
partition_ix = partition_axes[0]

with ops.name_scope(self._name + "/ConcatPartitions/"):
    concatenated = array_ops.concat(self._variable_list, partition_ix)

with ops.name_scope(None):
    exit(array_ops.identity(concatenated, name=self._name))
