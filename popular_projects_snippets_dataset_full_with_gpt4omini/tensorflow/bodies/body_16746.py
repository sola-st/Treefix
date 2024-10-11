# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Gets an existing variable with this name or create a new one."""
if regularizer is None:
    regularizer = self._regularizer
if caching_device is None:
    caching_device = self._caching_device
if partitioner is None:
    partitioner = self._partitioner
if custom_getter is None:
    custom_getter = self._custom_getter
if context.executing_eagerly():
    reuse = False
    use_resource = True
else:
    if reuse is None:
        reuse = self._reuse
    if use_resource is None:
        use_resource = self._use_resource

full_name = self.name + "/" + name if self.name else name
# Variable names only depend on variable_scope (full_name here),
# not name_scope, so we reset it below for the time of variable creation.
with ops.name_scope(None, skip_on_eager=False):
    # Check that `initializer` dtype and `dtype` are consistent before
    # replacing them with defaults.
    if (dtype is not None and initializer is not None and
        not callable(initializer)):
        init_dtype = ops.convert_to_tensor(initializer).dtype.base_dtype
        if init_dtype != dtype:
            raise ValueError("Initializer type '%s' and explicit dtype '%s' "
                             "don't match." % (init_dtype, dtype))
    if initializer is None:
        initializer = self._initializer
    if constraint is None:
        constraint = self._constraint
    if dtype is None:
        dtype = self._dtype
    exit(var_store.get_variable(
        full_name,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        regularizer=regularizer,
        reuse=reuse,
        trainable=trainable,
        collections=collections,
        caching_device=caching_device,
        partitioner=partitioner,
        validate_shape=validate_shape,
        use_resource=use_resource,
        custom_getter=custom_getter,
        constraint=constraint,
        synchronization=synchronization,
        aggregation=aggregation))
