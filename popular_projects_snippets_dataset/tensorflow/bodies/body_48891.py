# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
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
      - If the layer is not built, the method will call `build`.

    Raises:
      ValueError: if the layer's `call` method returns None (an invalid value).
      RuntimeError: if `super().__init__()` was not called in the constructor.
    """
if not hasattr(self, '_thread_local'):
    raise RuntimeError(
        'You must call `super().__init__()` in the layer constructor.')

# `inputs` (the first arg in the method spec) is special cased in
# layer call due to historical reasons.
# This special casing currently takes the form of:
# - 'inputs' must be explicitly passed. A layer cannot have zero arguments,
#   and inputs cannot have been provided via the default value of a kwarg.
# - numpy/scalar values in `inputs` get converted to tensors
# - implicit masks / mask metadata are only collected from 'inputs`
# - Layers are built using shape info from 'inputs' only
# - input_spec compatibility is only checked against `inputs`
# - mixed precision casting (autocast) is only applied to `inputs`,
#   not to any other argument.
# - setting the SavedModel saving spec.
inputs, args, kwargs = self._split_out_first_arg(args, kwargs)
input_list = nest.flatten(inputs)

# Functional Model construction mode is invoked when `Layer`s are called on
# symbolic `KerasTensor`s, i.e.:
# >> inputs = tf.keras.Input(10)
# >> outputs = MyLayer()(inputs)  # Functional construction mode.
# >> model = tf.keras.Model(inputs, outputs)
if _in_functional_construction_mode(self, inputs, args, kwargs, input_list):
    exit(self._functional_construction_call(inputs, args, kwargs,
                                              input_list))

# Maintains info about the `Layer.call` stack.
call_context = base_layer_utils.call_context()

# Accept NumPy and scalar inputs by converting to Tensors.
if any(isinstance(x, (
    np_arrays.ndarray, np.ndarray, float, int)) for x in input_list):
    inputs = nest.map_structure(_convert_numpy_or_python_types, inputs)
    input_list = nest.flatten(inputs)

# Handle `mask` propagation from previous layer to current layer. Masks can
# be propagated explicitly via the `mask` argument, or implicitly via
# setting the `_keras_mask` attribute on the inputs to a Layer. Masks passed
# explicitly take priority.
input_masks, mask_is_implicit = self._get_input_masks(
    inputs, input_list, args, kwargs)
if self._expects_mask_arg and mask_is_implicit:
    kwargs['mask'] = input_masks

# Training mode for `Layer.call` is set via (in order of priority):
# (1) The `training` argument passed to this `Layer.call`, if it is not None
# (2) The training mode of an outer `Layer.call`.
# (3) The default mode set by `tf.keras.backend.set_learning_phase` (if set)
# (4) Any non-None default value for `training` specified in the call
#  signature
# (5) False (treating the layer as if it's in inference)
args, kwargs, training_mode = self._set_training_mode(
    args, kwargs, call_context)

# Losses are cleared for all sublayers on the outermost `Layer.call`.
# Losses are not cleared on inner `Layer.call`s, because sublayers can be
# called multiple times.
if not call_context.in_call:
    self._clear_losses()

eager = context.executing_eagerly()
with call_context.enter(
    layer=self,
    inputs=inputs,
    build_graph=not eager,
    training=training_mode):

    input_spec.assert_input_compatibility(self.input_spec, inputs, self.name)
    if eager:
        call_fn = self.call
        name_scope = self._name
    else:
        name_scope = self._name_scope()  # Avoid autoincrementing.  # pylint: disable=not-callable
        call_fn = self._autographed_call()

    with ops.name_scope_v2(name_scope):
        if not self.built:
            self._maybe_build(inputs)

        if self._autocast:
            inputs = self._maybe_cast_inputs(inputs, input_list)

        with autocast_variable.enable_auto_cast_variables(
            self._compute_dtype_object):
            outputs = call_fn(inputs, *args, **kwargs)

        if self._activity_regularizer:
            self._handle_activity_regularization(inputs, outputs)
        if self._supports_masking:
            self._set_mask_metadata(inputs, outputs, input_masks, not eager)
        if self._saved_model_inputs_spec is None:
            self._set_save_spec(inputs)

        exit(outputs)
