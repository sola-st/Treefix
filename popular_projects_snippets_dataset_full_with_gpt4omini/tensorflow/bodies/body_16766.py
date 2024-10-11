# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Begins the scope block.

    Returns:
      A VariableScope.
    Raises:
      ValueError: when trying to reuse within a create scope, or create within
        a reuse scope, or if reuse is not `None` or `True`.
      TypeError: when the types of some arguments are not appropriate.
    """
self._old = self._var_scope_store.current_scope
if isinstance(self._name_or_scope, VariableScope):
    self._var_scope_store.open_variable_scope(self._new_name)
    self._old_subscopes = copy.copy(
        self._var_scope_store.variable_scopes_count)
    variable_scope_object = self._cached_variable_scope_object
else:
    # Handler for the case when we just prolong current variable scope.
    #   VariableScope with name extended by the provided one, and inherited
    #   reuse and initializer (except if the user provided values to set).
    self._new_name = (
        self._old.name + "/" +
        self._name_or_scope if self._old.name else self._name_or_scope)
    self._reuse = (self._reuse or
                   self._old.reuse)  # Re-using is inherited by sub-scopes.
    if self._old_name_scope is None:
        name_scope = self._name_or_scope
    else:
        name_scope = self._old_name_scope
    variable_scope_object = VariableScope(
        self._reuse,
        name=self._new_name,
        initializer=self._old.initializer,
        regularizer=self._old.regularizer,
        caching_device=self._old.caching_device,
        partitioner=self._old.partitioner,
        dtype=self._old.dtype,
        use_resource=self._old.use_resource,
        custom_getter=self._old.custom_getter,
        name_scope=name_scope,
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
                                      self._old.custom_getter))
    if self._dtype is not None:
        variable_scope_object.set_dtype(self._dtype)
    if self._use_resource is not None:
        variable_scope_object.set_use_resource(self._use_resource)
    self._var_scope_store.open_variable_scope(self._new_name)
self._var_scope_store.current_scope = variable_scope_object
self._last_variable_scope_object = variable_scope_object
exit(variable_scope_object)
