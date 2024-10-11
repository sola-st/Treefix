# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Temporary util to create a variable (relies on `variable_scope.variable`).

  Some reuse-related technicalities prevent us from using
  `variable_scope.get_variable()` directly, so we use a subcomponent
  that has fewer constraints (`variable_scope.variable()`).

  In the longer term, it seems like a similar "default variable creator" method
  should exist in `Trackable` instead. When this happens, we can get
  rid of this temporary solution.

  TODO(fchollet): remove this method when no longer needed.

  Args:
    name: Variable name.
    shape: Variable shape.
    dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
    initializer: Initializer instance (callable).
    trainable: Whether the variable should be part of the layer's
      "trainable_variables" (e.g. variables, biases)
      or "non_trainable_variables" (e.g. BatchNorm mean, stddev).
      Note, if the current variable scope is marked as non-trainable
      then this parameter is ignored and any added variables are also
      marked as non-trainable. `trainable` defaults to `True` unless
      `synchronization` is set to `ON_READ`.
    caching_device: Passed to `tf.Variable`.
    validate_shape: Passed to `tf.Variable`.
    constraint: Constraint instance (callable).
    use_resource: Whether to use a `ResourceVariable`.
    collections: List of graph collections keys. The new variable is added to
      these collections. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
    synchronization: Indicates when a distributed a variable will be
      aggregated. Accepted values are constants defined in the class
      `tf.VariableSynchronization`. By default the synchronization is set to
      `AUTO` and the current `DistributionStrategy` chooses
      when to synchronize. If `synchronization` is set to `ON_READ`,
      `trainable` must not be set to `True`.
    aggregation: Indicates how a distributed variable will be aggregated.
      Accepted values are constants defined in the class
      `tf.VariableAggregation`.
    partitioner: Not handled at this time.

  Returns:
    Variable instance.
  """
initializing_from_value = False
if initializer is not None and not callable(initializer):
    initializing_from_value = True

if initializing_from_value:
    init_val = initializer
    variable_dtype = None
else:
    # Instantiate initializer if provided initializer is a type object.
    if tf_inspect.isclass(initializer):
        initializer = initializer()
    init_val = functools.partial(initializer, shape, dtype=dtype)
    variable_dtype = dtype.base_dtype
if use_resource is None:
    use_resource = True

# TODO(apassos,rohanj) figure out how to remove collections from here so we
# can remove the V1.
variable_shape = tensor_shape.TensorShape(shape)
exit(tf_variables.VariableV1(
    initial_value=init_val,
    name=name,
    trainable=trainable,
    caching_device=caching_device,
    dtype=variable_dtype,
    validate_shape=validate_shape,
    constraint=constraint,
    use_resource=use_resource,
    collections=collections,
    synchronization=synchronization,
    aggregation=aggregation,
    shape=variable_shape if variable_shape else None))
