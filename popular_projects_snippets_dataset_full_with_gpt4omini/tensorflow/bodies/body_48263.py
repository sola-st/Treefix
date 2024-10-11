# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Wraps `call`, applying pre- and post-processing steps.

    Args:
      *args: Positional arguments to be passed to `self.call`.
      **kwargs: Keyword arguments to be passed to `self.call`.

    Returns:
      Output tensor(s).

    Note:
      - The following optional keyword arguments are reserved for specific uses:
        * `training`: Boolean scalar tensor of Python boolean indicating
          whether the `call` is meant for training or inference.
        * `mask`: Boolean input mask.
      - If the layer's `call` method takes a `mask` argument (as some Keras
        layers do), its default value will be set to the mask generated
        for `inputs` by the previous layer (if `input` did come from
        a layer that generated a corresponding mask, i.e. if it came from
        a Keras layer with masking support.

    Raises:
      ValueError: if the layer's `call` method returns None (an invalid value).
      RuntimeError: if `super().__init__()` was not called in the constructor.
    """
self._assert_built_as_v1()

if not hasattr(self, '_thread_local'):
    raise RuntimeError(
        'You must call `super().__init__()` in the layer constructor.')

# Grab the first positional or keyword argument.
if args:
    inputs = args[0]
    args = args[1:]
elif self._call_fn_args[0] in kwargs:
    inputs = kwargs.pop(self._call_fn_args[0])
else:
    raise ValueError(
        'The first argument to `Layer.call` must always be passed.')

call_context = base_layer_utils.call_context()
input_list = nest.flatten(inputs)

# We will attempt to build a TF graph if & only if all inputs are symbolic.
# This is always the case in graph mode. It can also be the case in eager
# mode when all inputs can be traced back to `keras.Input()` (when building
# models using the functional API).
build_graph = tf_utils.are_all_symbolic_tensors(input_list)

# Accept NumPy and scalar inputs by converting to Tensors.
if any(isinstance(x, (np.ndarray, float, int)) for x in input_list):
    def _convert_non_tensor(x):
        # Don't call `ops.convert_to_tensor` on all `inputs` because
        # `SparseTensors` can't be converted to `Tensor`.
        if isinstance(x, (np.ndarray, float, int)):
            exit(ops.convert_to_tensor_v2_with_dispatch(x))
        exit(x)
    inputs = nest.map_structure(_convert_non_tensor, inputs)
    input_list = nest.flatten(inputs)

# Handle `mask` propagation from previous layer to current layer. Masks can
# be propagated explicitly via the `mask` argument, or implicitly via
# setting the `_keras_mask` attribute on the inputs to a Layer. Masks passed
# explicitly take priority.
mask_arg_passed_by_framework = False
input_masks = self._collect_input_masks(inputs, args, kwargs)
if (self._expects_mask_arg and input_masks is not None and
    not self._call_arg_was_passed('mask', args, kwargs)):
    mask_arg_passed_by_framework = True
    kwargs['mask'] = input_masks

# If `training` argument is None or not explicitly passed,
# propagate `training` value from this layer's calling layer.
training_value = None
training_arg_passed_by_framework = False
# Priority 1: `training` was explicitly passed.
if self._call_arg_was_passed('training', args, kwargs):
    training_value = self._get_call_arg_value('training', args, kwargs)
    if not self._expects_training_arg:
        kwargs.pop('training')

if training_value is None:
    # Priority 2: `training` was passed to a parent layer.
    if call_context.training is not None:
        training_value = call_context.training
    # Priority 3a: `learning_phase()` has been set.
    elif backend.global_learning_phase_is_set():
        training_value = backend.learning_phase()
    # Priority 3b: Pass the `learning_phase()` if in the Keras FuncGraph.
    elif build_graph:
        with backend.get_graph().as_default():
            if base_layer_utils.is_in_keras_graph():
                training_value = backend.learning_phase()

    if self._expects_training_arg and training_value is not None:
        # Force the training_value to be bool type which matches to the contract
        # for layer/model call args.
        if tensor_util.is_tf_type(training_value):
            training_value = math_ops.cast(training_value, dtypes.bool)
        else:
            training_value = bool(training_value)
        args, kwargs = self._set_call_arg_value(
            'training', training_value, args, kwargs)
        training_arg_passed_by_framework = True

    # Only create Keras history if at least one tensor originates from a
    # `keras.Input`. Otherwise this Layer may be being used outside the Keras
    # framework.
if build_graph and base_layer_utils.needs_keras_history(inputs):
    base_layer_utils.create_keras_history(inputs)

with call_context.enter(self, inputs, build_graph, training_value):
    # Check input assumptions set after layer building, e.g. input shape.
    if build_graph:
        # Symbolic execution on symbolic tensors. We will attempt to build
        # the corresponding TF subgraph inside `backend.get_graph()`
        input_spec.assert_input_compatibility(self.input_spec, inputs,
                                              self.name)
        graph = backend.get_graph()
        with graph.as_default(), backend.name_scope(self._name_scope()):  # pylint: disable=not-callable
            # Build layer if applicable (if the `build` method has been
            # overridden).
            self._maybe_build(inputs)
            cast_inputs = self._maybe_cast_inputs(inputs)

            # Wrapping `call` function in autograph to allow for dynamic control
            # flow and control dependencies in call. We are limiting this to
            # subclassed layers as autograph is strictly needed only for
            # subclassed layers and models.
            # tf_convert will respect the value of autograph setting in the
            # enclosing tf.function, if any.
            if (base_layer_utils.is_subclassed(self) and
                not base_layer_utils.from_saved_model(self)):
                call_fn = autograph.tf_convert(
                    self.call, ag_ctx.control_status_ctx())
            else:
                call_fn = self.call

            if not self.dynamic:
                try:
                    with autocast_variable.enable_auto_cast_variables(
                        self._compute_dtype_object):
                        outputs = call_fn(cast_inputs, *args, **kwargs)

                except errors.OperatorNotAllowedInGraphError as e:
                    raise TypeError('You are attempting to use Python control '
                                    'flow in a layer that was not declared to be '
                                    'dynamic. Pass `dynamic=True` to the class '
                                    'constructor.\nEncountered error:\n"""\n' +
                                    str(e) + '\n"""')
            else:
                # We will use static shape inference to return symbolic tensors
                # matching the specifications of the layer outputs.
                # Since `self.dynamic` is True, we will never attempt to
                # run the underlying TF graph (which is disconnected).
                # TODO(fchollet): consider py_func as an alternative, which
                # would enable us to run the underlying graph if needed.
                outputs = self._symbolic_call(inputs)

            if outputs is None:
                raise ValueError('A layer\'s `call` method should return a '
                                 'Tensor or a list of Tensors, not None '
                                 '(layer: ' + self.name + ').')
            if base_layer_utils.have_all_keras_metadata(inputs):
                if training_arg_passed_by_framework:
                    args, kwargs = self._set_call_arg_value(
                        'training', None, args, kwargs, pop_kwarg_if_none=True)
                if mask_arg_passed_by_framework:
                    kwargs.pop('mask')
                outputs = self._set_connectivity_metadata((inputs,) + args, kwargs,
                                                          outputs)
            self._handle_activity_regularization(inputs, outputs)
            self._set_mask_metadata(inputs, outputs, input_masks)
            if hasattr(self, '_set_inputs') and not self.inputs:
                # Subclassed network: explicitly set metadata normally set by
                # a call to self._set_inputs().
                # TODO(b/120997007): This should be done in Eager as well, but
                # causes garbage collection issues because of the placeholders
                # created on the default Keras graph.
                self._set_inputs(inputs, outputs)
    else:
        # Eager execution on data tensors.
        with backend.name_scope(self._name_scope()):  # pylint: disable=not-callable
            self._maybe_build(inputs)
            cast_inputs = self._maybe_cast_inputs(inputs)
            with autocast_variable.enable_auto_cast_variables(
                self._compute_dtype_object):
                outputs = self.call(cast_inputs, *args, **kwargs)
            self._handle_activity_regularization(inputs, outputs)
            self._set_mask_metadata(inputs, outputs, input_masks)

exit(outputs)
