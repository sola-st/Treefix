# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Creates a context for the variable_scope, see `variable_scope` for docs.

    Note: this does not create a name scope.

    Args:
      name_or_scope: `string` or `VariableScope`: the scope to open.
      reuse: `True` or None, or tf.compat.v1.AUTO_REUSE; if `None`, we inherit
        the parent scope's reuse flag.
      initializer: default initializer for variables within this scope.
      regularizer: default regularizer for variables within this scope.
      caching_device: default caching device for variables within this scope.
      partitioner: default partitioner for variables within this scope.
      custom_getter: default custom getter for variables within this scope.
      old_name_scope: the original name scope when re-entering a variable scope.
      dtype: type of the variables within this scope (defaults to `DT_FLOAT`).
      use_resource: If False, variables in this scope will be regular Variables.
        If True, experimental ResourceVariables will be creates instead, with
        well-defined semantics. Defaults to False (will later change to True).
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
    """
self._name_or_scope = name_or_scope
self._reuse = reuse
self._initializer = initializer
self._regularizer = regularizer
self._caching_device = caching_device
self._partitioner = partitioner
self._custom_getter = custom_getter
self._old_name_scope = old_name_scope
self._dtype = dtype
self._use_resource = use_resource
self._constraint = constraint
self._var_store = _get_default_variable_store()
self._var_scope_store = get_variable_scope_store()
self._last_variable_scope_object = None
if isinstance(self._name_or_scope, VariableScope):
    self._new_name = self._name_or_scope.name
    name_scope = self._name_or_scope._name_scope  # pylint: disable=protected-access
    # Handler for the case when we jump to a shared scope.  We create a new
    #   VariableScope (self._var_scope_object) that contains a copy of the
    #   provided shared scope, possibly with changed reuse and initializer, if
    #   the user requested this.
    variable_scope_object = VariableScope(
        self._name_or_scope.reuse if not self._reuse else self._reuse,
        name=self._new_name,
        initializer=self._name_or_scope.initializer,
        regularizer=self._name_or_scope.regularizer,
        caching_device=self._name_or_scope.caching_device,
        partitioner=self._name_or_scope.partitioner,
        dtype=self._name_or_scope.dtype,
        custom_getter=self._name_or_scope.custom_getter,
        name_scope=name_scope,
        use_resource=self._name_or_scope.use_resource,
        constraint=self._constraint)
    if self._initializer is not None:
        variable_scope_object.set_initializer(self._initializer)
    if self._regularizer is not None:
        variable_scope_object.set_regularizer(self._regularizer)
    if self._caching_device is not None:
        variable_scope_object.set_caching_device(self._caching_device)
    if self._partitioner is not None:
        variable_scope_object.set_partitioner(self._partitioner)
    if self._custom_getter is not None:
        variable_scope_object.set_custom_getter(
            _maybe_wrap_custom_getter(self._custom_getter,
                                      self._name_or_scope.custom_getter))
    if self._dtype is not None:
        variable_scope_object.set_dtype(self._dtype)
    if self._use_resource is not None:
        variable_scope_object.set_use_resource(self._use_resource)
    self._cached_variable_scope_object = variable_scope_object
