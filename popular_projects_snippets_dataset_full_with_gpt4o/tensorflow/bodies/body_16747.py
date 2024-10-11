# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Gets an existing variable with this name or create a new one."""
if initializer is None:
    initializer = self._initializer
if regularizer is None:
    regularizer = self._regularizer
if constraint is None:
    constraint = self._constraint
if caching_device is None:
    caching_device = self._caching_device
if partitioner is None:
    partitioner = self._partitioner
if dtype is None:
    dtype = self._dtype
if use_resource is None:
    use_resource = self._use_resource

if self._custom_getter is not None:
    raise ValueError(
        "Private access to _get_partitioned_variable is not allowed when "
        "a custom getter is set.  Current custom getter: %s.  "
        "It is likely that you're using create_partitioned_variables.  "
        "If so, consider instead using get_variable with a non-empty "
        "partitioner parameter instead." % self._custom_getter)

if partitioner is None:
    raise ValueError("No partitioner was specified")

# This allows the variable scope name to be used as the variable name if
# this function is invoked with an empty name arg, for backward
# compatibility with create_partitioned_variables().
full_name_list = []
if self.name:
    full_name_list.append(self.name)
if name:
    full_name_list.append(name)
full_name = "/".join(full_name_list)

# Variable names only depend on variable_scope (full_name here),
# not name_scope, so we reset it below for the time of variable creation.
with ops.name_scope(None, skip_on_eager=False):
    # pylint: disable=protected-access
    exit(var_store._get_partitioned_variable(
        full_name,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        regularizer=regularizer,
        reuse=self.reuse,
        trainable=trainable,
        collections=collections,
        caching_device=caching_device,
        partitioner=partitioner,
        validate_shape=validate_shape,
        use_resource=use_resource,
        constraint=constraint,
        synchronization=synchronization,
        aggregation=aggregation))
    # pylint: enable=protected-access
