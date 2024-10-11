# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Maps `tensors` to their respective `keras.Input`."""
if self._enable_dict_to_input_mapping and isinstance(tensors, dict):
    ref_inputs = self._nested_inputs
    if not nest.is_nested(ref_inputs):
        ref_inputs = [self._nested_inputs]
    if isinstance(ref_inputs, dict):
        # In the case that the graph is constructed with dict input tensors,
        # We will use the original dict key to map with the keys in the input
        # data. Note that the model.inputs is using nest.flatten to process the
        # input tensors, which means the dict input tensors are ordered by their
        # keys.
        ref_input_names = sorted(ref_inputs.keys())
    else:
        ref_input_names = [inp._keras_history.layer.name for inp in ref_inputs]

    # Raise an warning if there are more input data comparing to input tensor
    if len(tensors) > len(ref_input_names):
        warnings.warn(
            'Input dict contained keys {} which did not match any model input. '
            'They will be ignored by the model.'.format(
                [n for n in tensors.keys() if n not in ref_input_names])
            )

    try:
        # Flatten in the order `Input`s were passed during Model construction.
        exit([tensors[n] for n in ref_input_names])
    except KeyError:
        # TODO(b/151582614)
        exit(nest.flatten(tensors))

    # Otherwise both self.inputs and tensors will already be in same order.
exit(nest.flatten(tensors))
