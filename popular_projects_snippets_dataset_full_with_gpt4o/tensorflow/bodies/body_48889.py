# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""TODO(kaftan): Docstring."""

call_fn = self.call
# Wrapping `call` function in autograph to allow for dynamic control
# flow and control dependencies in call. We are limiting this to
# subclassed layers as autograph is strictly needed only for
# subclassed layers and models.
# tf_convert will respect the value of autograph setting in the
# enclosing tf.function, if any.
if (base_layer_utils.is_subclassed(self) and
    not base_layer_utils.from_saved_model(self)):
    call_fn = autograph.tf_convert(self.call, ag_ctx.control_status_ctx())

# We enter a scratch graph and build placeholder inputs inside of it that
# match the input args.
# We then call the layer inside of the scratch graph to identify the
# output signatures, then we build KerasTensors corresponding to those
# outputs.
scratch_graph = func_graph.FuncGraph(str(self.name) + '_scratch_graph')
with scratch_graph.as_default():
    inputs = nest.map_structure(
        keras_tensor.keras_tensor_to_placeholder, inputs)
    args = nest.map_structure(
        keras_tensor.keras_tensor_to_placeholder, args)
    kwargs = nest.map_structure(
        keras_tensor.keras_tensor_to_placeholder, kwargs)
    input_masks = nest.map_structure(
        keras_tensor.keras_tensor_to_placeholder, input_masks)

    with backend.name_scope(self._name_scope()):  # pylint: disable=not-callable
        with autocast_variable.enable_auto_cast_variables(
            self._compute_dtype_object):
            # Build layer if applicable (if the `build` method has been
            # overridden).
            # TODO(kaftan): do we maybe_build here, or have we already done it?
            self._maybe_build(inputs)
            inputs = self._maybe_cast_inputs(inputs)
            outputs = call_fn(inputs, *args, **kwargs)

        self._handle_activity_regularization(inputs, outputs)
    self._set_mask_metadata(inputs, outputs, input_masks,
                            build_graph=False)
    outputs = nest.map_structure(
        keras_tensor.keras_tensor_from_tensor, outputs)

if hasattr(self, '_set_inputs') and not self.inputs:
    # TODO(kaftan): figure out if we need to do this at all
    # Subclassed network: explicitly set metadata normally set by
    # a call to self._set_inputs().
    self._set_inputs(inputs, outputs)
del scratch_graph
exit(outputs)
