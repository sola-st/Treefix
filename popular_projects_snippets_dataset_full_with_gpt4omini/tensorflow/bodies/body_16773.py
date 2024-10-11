# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Enters the context manager when there is no cached scope yet.

    Returns:
      The entered variable scope.

    Raises:
      TypeError: A wrong type is passed as `scope` at __init__().
      ValueError: `reuse` is incorrectly set at __init__().
    """
if self._auxiliary_name_scope:
    # Create a new name scope later
    current_name_scope = None
else:
    # Reenter the current name scope
    name_scope = ops.get_name_scope()
    if name_scope:
        # Hack to reenter
        name_scope += "/"
        current_name_scope = ops.name_scope(name_scope, skip_on_eager=False)
    else:
        # Root scope
        current_name_scope = ops.name_scope(name_scope, skip_on_eager=False)

    # IMPORTANT: Only assign to self._cached_pure_variable_scope and
    # self._current_name_scope after successful __enter__() calls.
if self._name_or_scope is not None:
    if not isinstance(self._name_or_scope, (VariableScope, str)):
        raise TypeError("VariableScope: name_or_scope must be a string or "
                        "VariableScope.")
    if isinstance(self._name_or_scope, str):
        name_scope = self._name_or_scope
    else:
        name_scope = self._name_or_scope.name.split("/")[-1]
    if name_scope or current_name_scope:
        current_name_scope = current_name_scope or ops.name_scope(
            name_scope, skip_on_eager=False)
        try:
            current_name_scope_name = current_name_scope.__enter__()
        except:
            current_name_scope.__exit__(*sys.exc_info())
            raise
        self._current_name_scope = current_name_scope
        if isinstance(self._name_or_scope, str):
            old_name_scope = current_name_scope_name
        else:
            old_name_scope = self._name_or_scope.original_name_scope
        pure_variable_scope = _pure_variable_scope(
            self._name_or_scope,
            reuse=self._reuse,
            initializer=self._initializer,
            regularizer=self._regularizer,
            caching_device=self._caching_device,
            partitioner=self._partitioner,
            custom_getter=self._custom_getter,
            old_name_scope=old_name_scope,
            dtype=self._dtype,
            use_resource=self._use_resource,
            constraint=self._constraint)
        try:
            entered_pure_variable_scope = pure_variable_scope.__enter__()
        except:
            pure_variable_scope.__exit__(*sys.exc_info())
            raise
        self._cached_pure_variable_scope = pure_variable_scope
        exit(entered_pure_variable_scope)
    else:
        self._current_name_scope = None
        # This can only happen if someone is entering the root variable scope.
        pure_variable_scope = _pure_variable_scope(
            self._name_or_scope,
            reuse=self._reuse,
            initializer=self._initializer,
            regularizer=self._regularizer,
            caching_device=self._caching_device,
            partitioner=self._partitioner,
            custom_getter=self._custom_getter,
            dtype=self._dtype,
            use_resource=self._use_resource,
            constraint=self._constraint)
        try:
            entered_pure_variable_scope = pure_variable_scope.__enter__()
        except:
            pure_variable_scope.__exit__(*sys.exc_info())
            raise
        self._cached_pure_variable_scope = pure_variable_scope
        exit(entered_pure_variable_scope)

else:  # Here name_or_scope is None. Using default name, but made unique.
    if self._reuse:
        raise ValueError("reuse=True cannot be used without a name_or_scope")
    current_name_scope = current_name_scope or ops.name_scope(
        self._default_name, skip_on_eager=False)
    try:
        current_name_scope_name = current_name_scope.__enter__()
    except:
        current_name_scope.__exit__(*sys.exc_info())
        raise
    self._current_name_scope = current_name_scope
    unique_default_name = _get_unique_variable_scope(self._default_name)
    pure_variable_scope = _pure_variable_scope(
        unique_default_name,
        initializer=self._initializer,
        regularizer=self._regularizer,
        caching_device=self._caching_device,
        partitioner=self._partitioner,
        custom_getter=self._custom_getter,
        old_name_scope=current_name_scope_name,
        dtype=self._dtype,
        use_resource=self._use_resource,
        constraint=self._constraint)
    try:
        entered_pure_variable_scope = pure_variable_scope.__enter__()
    except:
        pure_variable_scope.__exit__(*sys.exc_info())
        raise
    self._cached_pure_variable_scope = pure_variable_scope
    exit(entered_pure_variable_scope)
