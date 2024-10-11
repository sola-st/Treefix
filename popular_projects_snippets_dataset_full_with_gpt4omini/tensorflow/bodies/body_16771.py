# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Initialize the context manager.

    Args:
      name_or_scope: `string` or `VariableScope`: the scope to open.
      default_name: The default name to use if the `name_or_scope` argument is
        `None`, this name will be uniquified. If name_or_scope is provided it
        won't be used and therefore it is not required and can be None.
      values: The list of `Tensor` arguments that are passed to the op function.
      initializer: default initializer for variables within this scope.
      regularizer: default regularizer for variables within this scope.
      caching_device: default caching device for variables within this scope.
      partitioner: default partitioner for variables within this scope.
      custom_getter: default custom getter for variables within this scope.
      reuse: `True`, None, or tf.compat.v1.AUTO_REUSE; if `True`, we go into
        reuse mode for this scope as well as all sub-scopes; if
        tf.compat.v1.AUTO_REUSE, we create variables if they do not exist, and
        return them otherwise; if None, we inherit the parent scope's reuse
        flag. When eager execution is enabled, new variables are always created
        unless an EagerVariableStore or template is currently active.
      dtype: type of variables created in this scope (defaults to the type in
        the passed scope, or inherited from parent scope).
      use_resource: If False, all variables will be regular Variables. If True,
        experimental ResourceVariables with well-defined semantics will be used
        instead. Defaults to False (will later change to True). When eager
        execution is enabled this argument is always forced to be True.
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
      auxiliary_name_scope: If `True`, we create an auxiliary name scope with
        the scope. If `False`, we don't create it. Note that the argument is not
        inherited, and it only takes effect for once when creating. You should
        only use it for re-entering a premade variable scope.

    Returns:
      A scope that can be captured and reused.

    Raises:
      ValueError: when trying to reuse within a create scope, or create within
        a reuse scope.
      TypeError: when the types of some arguments are not appropriate.
    """
self._name_or_scope = name_or_scope
self._default_name = default_name
self._values = values
self._initializer = initializer
self._regularizer = regularizer
self._caching_device = caching_device
self._partitioner = partitioner
self._custom_getter = custom_getter
self._reuse = reuse
self._dtype = dtype
self._use_resource = use_resource
self._constraint = constraint
if self._default_name is None and self._name_or_scope is None:
    raise TypeError("If default_name is None then name_or_scope is required")
if self._reuse is False:
    # We don't allow non-inheriting scopes, False = None here.
    self._reuse = None
if not (self._reuse is True
        or self._reuse is None
        or self._reuse is AUTO_REUSE):
    raise ValueError("The reuse parameter must be True or False or None.")
if self._values is None:
    self._values = []
self._in_graph_mode = not context.executing_eagerly()
if self._in_graph_mode:
    self._graph = ops._get_graph_from_inputs(self._values)  # pylint: disable=protected-access
self._cached_pure_variable_scope = None
self._current_name_scope = None
if not isinstance(auxiliary_name_scope, bool):
    raise TypeError("The auxiliary_name_scope must be `True` or `False`, "
                    "while get {}".format(auxiliary_name_scope))
self._auxiliary_name_scope = auxiliary_name_scope
