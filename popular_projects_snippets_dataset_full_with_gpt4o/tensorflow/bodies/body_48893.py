# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
call_context = base_layer_utils.call_context()

# Accept NumPy and scalar inputs by converting to Tensors.
if any(isinstance(x, (
    np_arrays.ndarray, np.ndarray, float, int)) for x in input_list):

    def _convert_non_tensor(x):
        # Don't call `ops.convert_to_tensor` on all `inputs` because
        # `SparseTensors` can't be converted to `Tensor`.
        if isinstance(x, (np_arrays.ndarray, np.ndarray, float, int)):
            exit(ops.convert_to_tensor_v2_with_dispatch(x))
        exit(x)

    inputs = nest.map_structure(_convert_non_tensor, inputs)
    input_list = nest.flatten(inputs)

# Handle `mask` propagation from previous layer to current layer. Masks can
# be propagated explicitly via the `mask` argument, or implicitly via
# setting the `_keras_mask` attribute on the inputs to a Layer. Masks passed
# explicitly take priority.
mask_arg_passed_by_framework = False
input_masks, mask_is_implicit = self._get_input_masks(
    inputs, input_list, args, kwargs)
if self._expects_mask_arg and mask_is_implicit:
    kwargs['mask'] = input_masks
    mask_arg_passed_by_framework = True

# If `training` argument is None or not explicitly passed,
# propagate `training` value from this layer's calling layer.
training_value = None
training_arg_passed_by_framework = False
# Priority 1: `training` was explicitly passed a non-None value.
if self._call_arg_was_passed('training', args, kwargs):
    training_value = self._get_call_arg_value('training', args, kwargs)
    if not self._expects_training_arg:
        kwargs.pop('training')

if training_value is None:
    # Priority 2: `training` was passed to a parent layer.
    if call_context.training is not None:
        training_value = call_context.training
    # Priority 3: `learning_phase()` has been set.
    elif backend.global_learning_phase_is_set():
        training_value = backend.learning_phase()
        # Force the training_value to be bool type which matches to the contract
        # for layer/model call args.
        if tensor_util.is_tf_type(training_value):
            training_value = math_ops.cast(training_value, dtypes.bool)
        else:
            training_value = bool(training_value)
      # Priority 4: trace layer with the default training argument specified
      # in the `call` signature (or in inference mode if the `call` signature
      # specifies no non-None default).
    else:
        training_value = self._default_training_arg
    # In cases (2), (3), (4) the training argument is passed automatically
    # by the framework, and will not be hard-coded into the model.
    if self._expects_training_arg:
        args, kwargs = self._set_call_arg_value('training', training_value,
                                                args, kwargs)
        training_arg_passed_by_framework = True

with call_context.enter(
    layer=self, inputs=inputs, build_graph=True, training=training_value):
    # Check input assumptions set after layer building, e.g. input shape.
    outputs = self._keras_tensor_symbolic_call(
        inputs, input_masks, args, kwargs)

    if outputs is None:
        raise ValueError('A layer\'s `call` method should return a '
                         'Tensor or a list of Tensors, not None '
                         '(layer: ' + self.name + ').')
    if training_arg_passed_by_framework:
        args, kwargs = self._set_call_arg_value(
            'training', None, args, kwargs, pop_kwarg_if_none=True)
    if mask_arg_passed_by_framework:
        kwargs.pop('mask')
    # Node connectivity does not special-case the first argument.
    outputs = self._set_connectivity_metadata((inputs,) + args, kwargs,
                                              outputs)
    exit(outputs)
