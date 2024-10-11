# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
partition_axes = self._partition_axes()
if len(partition_axes) > 1:
    raise NotImplementedError(
        "Cannot do assign action along more than one dimension: %s.  "
        "Multi-axis partition assign action is not supported " %
        str(partition_axes))
if isinstance(value, list):
    assert len(value) == len(self._variable_list)
    value_list = value
elif isinstance(value, PartitionedVariable):
    value_list = [var_part for var_part in value]
else:
    partition_ix = partition_axes[0]
    size_splits_list = [
        tensor_shape.dimension_value(var.shape[partition_ix])
        for var in self._variable_list
    ]
    value_list = array_ops.split(value, size_splits_list, axis=partition_ix)

op_list = [
    assign_fn(var, value_list[idx])
    for idx, var in enumerate(self._variable_list)
]
exit(op_list)
