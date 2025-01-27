# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
"""Get or create a single Variable (e.g.

    a shard or entire variable).

    See the documentation of get_variable above (ignore partitioning components)
    for details.

    Args:
      name: see get_variable.
      shape: see get_variable.
      dtype: see get_variable.
      initializer: see get_variable.
      regularizer: see get_variable.
      partition_info: _PartitionInfo object.
      reuse: see get_variable.
      trainable: see get_variable.
      caching_device: see get_variable.
      validate_shape: see get_variable.
      constraint: see get_variable.
      synchronization: see get_variable.
      aggregation: see get_variable.

    Returns:
      A Variable.  See documentation of get_variable above.

    Raises:
      ValueError: See documentation of get_variable above.
    """
# Set to true if initializer is a constant.
initializing_from_value = False
if initializer is not None and not callable(initializer):
    initializing_from_value = True
if shape is not None and initializing_from_value:
    raise ValueError("If initializer is a constant, do not specify shape.")

dtype = dtypes.as_dtype(dtype)
shape = as_shape(shape)

if name in self._vars:
    # Here we handle the case when returning an existing variable.
    if reuse is False:  # pylint: disable=g-bool-id-comparison
        err_msg = ("Variable %s already exists, disallowed."
                   " Did you mean to set reuse=True or "
                   "reuse=tf.AUTO_REUSE in VarScope?" % name)
        # ResourceVariables don't have an op associated with so no traceback
        raise ValueError(err_msg)
    found_var = self._vars[name]
    if not shape.is_compatible_with(found_var.get_shape()):
        raise ValueError("Trying to share variable %s, but specified shape %s"
                         " and found shape %s." %
                         (name, shape, found_var.get_shape()))
    if not dtype.is_compatible_with(found_var.dtype):
        dtype_str = dtype.name
        found_type_str = found_var.dtype.name
        raise ValueError("Trying to share variable %s, but specified dtype %s"
                         " and found dtype %s." %
                         (name, dtype_str, found_type_str))
    exit(found_var)

# The code below handles only the case of creating a new variable.
if reuse is True:  # pylint: disable=g-bool-id-comparison
    raise ValueError("Variable %s does not exist, or was not created with "
                     "tf.get_variable(). Did you mean to set "
                     "reuse=tf.AUTO_REUSE in VarScope?" % name)

# Create the tensor to initialize the variable with default value.
if initializer is None:
    initializer, initializing_from_value = self._get_default_initializer(
        name=name, shape=shape, dtype=dtype)
# Enter an init scope when creating the initializer.
with ops.init_scope():
    if initializing_from_value:
        init_val = initializer
        variable_dtype = None
    else:
        # Instantiate initializer if provided initializer is a type object.
        if tf_inspect.isclass(initializer):
            initializer = initializer()
        if shape.is_fully_defined():
            if "partition_info" in tf_inspect.getargspec(initializer).args:
                init_val = functools.partial(initializer,
                                             shape.as_list(),
                                             dtype=dtype,
                                             partition_info=partition_info)
            else:
                init_val = functools.partial(initializer,
                                             shape.as_list(), dtype=dtype)
            variable_dtype = dtype.base_dtype
        else:
            init_val = initializer
            variable_dtype = None

    # Create the variable (Always eagerly as a workaround for a strange
    # tpu / funcgraph / keras functional model interaction )
with ops.init_scope():
    v = variables.Variable(
        initial_value=init_val,
        name=name,
        trainable=trainable,
        caching_device=caching_device,
        dtype=variable_dtype,
        validate_shape=validate_shape,
        constraint=constraint,
        synchronization=synchronization,
        aggregation=aggregation)

self._vars[name] = v
logging.vlog(1, "Created variable %s with shape %s and init %s", v.name,
             format(shape), initializer)

# Run the regularizer if requested and save the resulting loss.
if regularizer:
    self.add_regularizer(v, regularizer)

exit(v)
