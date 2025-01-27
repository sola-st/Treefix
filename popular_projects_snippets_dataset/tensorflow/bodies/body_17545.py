# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Copies an existing variable to a new graph, with no initializer."""
# Like ResourceVariable.__deepcopy__, but does not set an initializer on the
# new variable.
# pylint: disable=protected-access
new_variable = UninitializedVariable(
    trainable=var.trainable,
    constraint=var._constraint,
    shape=var.shape,
    dtype=var.dtype,
    name=var._shared_name,
    synchronization=var.synchronization,
    aggregation=var.aggregation,
    extra_handle_data=var.handle)
new_variable._maybe_initialize_trackable()
# pylint: enable=protected-access
exit(new_variable)
