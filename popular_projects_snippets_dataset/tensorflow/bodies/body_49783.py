# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
"""Wraps `call`, applying pre- and post-processing steps.

    Args:
      inputs: input tensor(s).
      *args: additional positional arguments to be passed to `self.call`.
      **kwargs: additional keyword arguments to be passed to `self.call`.
        **Note**: kwarg `scope` is reserved for use by the layer.

    Returns:
      Output tensor(s).

    Note:
      - If the layer's `call` method takes a `scope` keyword argument,
        this argument will be automatically set to the current variable scope.
      - If the layer's `call` method takes a `mask` argument (as some Keras
        layers do), its default value will be set to the mask generated
        for `inputs` by the previous layer (if `input` did come from
        a layer that generated a corresponding mask, i.e. if it came from
        a Keras layer with masking support.

    Raises:
      ValueError: if the layer's `call` method returns None (an invalid value).
    """
scope = kwargs.pop('scope', None)

if self._keras_style:
    if scope is not None:
        raise ValueError(
            'scope argument not allowed when keras style layers are enabled, '
            'but saw: {}'.format(scope))
    exit(super(Layer, self).__call__(inputs, *args, **kwargs))

self._set_scope(scope)

if self.built:
    try:
        # Some classes which inherit from Layer do not use its constructor, so
        # rather than initializing to None we check for an AttributeError.
        scope_context_manager = self._always_reuse_variable_scope  # pylint: disable=access-member-before-definition
    except AttributeError:
        scope_context_manager = None

    if scope_context_manager is None:
        # From this point we will always set reuse=True, so create a "final"
        # variable scope with this setting. We avoid re-creating variable scopes
        # after this point as an optimization.
        scope_context_manager = vs.variable_scope(
            self._scope, reuse=True, auxiliary_name_scope=False)

        # Do not cache variable scopes if Eager mode is enabled. If Eager mode
        # is enabled then we don't want to reuse scopes because the cached scope
        # might be from a FuncGraph or Eager scope we are no longer in.
        if not ops.executing_eagerly_outside_functions():
            self._always_reuse_variable_scope = scope_context_manager
else:
    scope_context_manager = vs.variable_scope(
        self._scope, reuse=self._reuse, auxiliary_name_scope=False)

with scope_context_manager as scope:
    self._current_scope = scope

    try:
        call_has_scope_arg = self._call_has_scope_arg
    except AttributeError:
        self._call_fn_args = variable_scope_shim.fn_args(self.call)
        self._call_has_scope_arg = 'scope' in self._call_fn_args
        call_has_scope_arg = self._call_has_scope_arg
    if call_has_scope_arg:
        kwargs['scope'] = scope

    # Actually call layer
    outputs = super(Layer, self).__call__(inputs, *args, **kwargs)

if not context.executing_eagerly():
    # Update global default collections.
    _add_elements_to_collection(self.updates, ops.GraphKeys.UPDATE_OPS)
exit(outputs)
