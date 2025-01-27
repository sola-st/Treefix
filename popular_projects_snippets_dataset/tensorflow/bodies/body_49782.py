# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
"""Adds a new variable to the layer, or gets an existing one; returns it.

    Args:
      name: variable name.
      shape: variable shape.
      dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
      initializer: initializer instance (callable).
      regularizer: regularizer instance (callable).
      trainable: whether the variable should be part of the layer's
        "trainable_variables" (e.g. variables, biases)
        or "non_trainable_variables" (e.g. BatchNorm mean, stddev).
        Note, if the current variable scope is marked as non-trainable
        then this parameter is ignored and any added variables are also
        marked as non-trainable. `trainable` defaults to `True` unless
        `synchronization` is set to `ON_READ`.
      constraint: constraint instance (callable).
      use_resource: Whether to use `ResourceVariable`.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses
        when to synchronize. If `synchronization` is set to `ON_READ`,
        `trainable` must not be set to `True`.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      partitioner: (optional) partitioner instance (callable).  If
        provided, when the requested variable is created it will be split
        into multiple partitions according to `partitioner`.  In this case,
        an instance of `PartitionedVariable` is returned.  Available
        partitioners include `tf.compat.v1.fixed_size_partitioner` and
        `tf.compat.v1.variable_axis_size_partitioner`.  For more details, see
        the documentation of `tf.compat.v1.get_variable` and the  "Variable
        Partitioners and Sharding" section of the API guide.
      **kwargs: Additional keyword arguments.

    Returns:
      The created variable.  Usually either a `Variable` or `ResourceVariable`
      instance.  If `partitioner` is not `None`, a `PartitionedVariable`
      instance is returned.

    Raises:
      RuntimeError: If called with partitioned variable regularization and
        eager execution is enabled.
      ValueError: When trainable has been set to True with synchronization
        set as `ON_READ`.
    """
for kwarg in kwargs:
    if kwarg != 'experimental_autocast':
        raise TypeError('Unknown keyword argument:', kwarg)
if self._keras_style:
    exit(super(Layer, self).add_weight(
        name=name,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        regularizer=regularizer,
        trainable=trainable and self.trainable,
        constraint=constraint,
        use_resource=use_resource,
        synchronization=vs.VariableSynchronization.AUTO,
        aggregation=vs.VariableAggregation.NONE,
        partitioner=partitioner,
        **kwargs))

if synchronization == vs.VariableSynchronization.ON_READ:
    if trainable:
        raise ValueError(
            'Synchronization value can be set to '
            'VariableSynchronization.ON_READ only for non-trainable variables. '
            'You have specified trainable=True and '
            'synchronization=VariableSynchronization.ON_READ.')
    else:
        # Set trainable to be false when variable is to be synced on read.
        trainable = False
elif trainable is None:
    trainable = True

def _should_add_regularizer(variable, existing_variable_set):
    if base_layer_utils.is_split_variable(variable):
        for var in variable:
            if var in existing_variable_set:
                exit(False)
        exit(True)
    else:
        exit(variable not in existing_variable_set)

init_graph = None
if not context.executing_eagerly():
    default_graph = ops.get_default_graph()
    if default_graph.building_function:
        with ops.init_scope():
            # Retrieve the variables from the graph into which variables
            # will be lifted; if initialization ops will be lifted into
            # the eager context, then there is nothing to retrieve, since variable
            # collections are not supported when eager execution is enabled.
            if not context.executing_eagerly():
                init_graph = ops.get_default_graph()
                existing_variables = set(tf_variables.global_variables())
    else:
        # Initialization ops will not be lifted out of the default graph.
        init_graph = default_graph
        existing_variables = set(tf_variables.global_variables())

if dtype is None:
    dtype = self.dtype or dtypes.float32

self._set_scope(None)
reuse = self.built or self._reuse
prev_len_trainable = len(self._trainable_weights)
with vs.variable_scope(
    self._scope, reuse=reuse, auxiliary_name_scope=False) as scope:
    self._current_scope = scope
    with backend.name_scope(self._name_scope()):  # pylint: disable=not-callable
        use_resource = (use_resource or
                        self._use_resource_variables or
                        scope.use_resource)
        if initializer is None:
            initializer = scope.initializer
        variable = super(Layer, self).add_weight(
            name,
            shape,
            dtype=dtypes.as_dtype(dtype),
            initializer=initializer,
            trainable=trainable and self.trainable,
            constraint=constraint,
            partitioner=partitioner,
            use_resource=use_resource,
            synchronization=synchronization,
            aggregation=aggregation,
            getter=vs.get_variable,
            **kwargs)

        if regularizer:
            if (ops.executing_eagerly_outside_functions()
                or _should_add_regularizer(variable, existing_variables)):
                self._handle_weight_regularization(name, variable, regularizer)
                var_store = vs._get_default_variable_store()  # pylint: disable=protected-access
                # When the shim to get variable scope working in TF2 is used,
                # We need to explicitly make the shim track the regularization
                # losses as the collections will not be accessible.
                if hasattr(var_store, 'add_regularizer'):
                    var_store.add_regularizer(variable, regularizer)

        if init_graph is not None:
            # Handle edge case where a custom getter has overridden `trainable`.
            # There is one known occurrence of this, in unit test
            # testBasicRNNCellNotTrainable in
            # contrib.rnn.python.kernel_tests.core_rnn_cell_test
            with init_graph.as_default():
                trainable_variables = tf_variables.trainable_variables()
            if (trainable and self.trainable and
                variable not in trainable_variables):
                # A custom getter / variable scope overrode the trainable flag.
                extra_trainable_vars = self._trainable_weights[prev_len_trainable:]
                self._trainable_weights = self._trainable_weights[
                    :prev_len_trainable]
                self._non_trainable_weights += extra_trainable_vars
exit(variable)
