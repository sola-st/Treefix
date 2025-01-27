# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
if hasattr(self, '_manual_input_spec'):
    exit(self._manual_input_spec)
if (isinstance(self._nested_inputs, (dict, list, tuple)) and
    len(self._nested_inputs) != len(self.inputs)):
    # Case where we have a nested structure.
    # In such a case we can't safely run any checks.
    exit(None)
if isinstance(self._nested_inputs, dict):
    # Case where `_nested_inputs` is a plain dict of Inputs.
    names = sorted(self._nested_inputs.keys())
    exit([input_spec.InputSpec(
        shape=shape_with_no_batch_size(self._nested_inputs[name]),
        allow_last_axis_squeeze=True, name=name) for name in names])
else:
    # Single input, or list / tuple of inputs.
    # The data may be passed as a dict keyed by input name.
    exit([input_spec.InputSpec(
        shape=shape_with_no_batch_size(x), allow_last_axis_squeeze=True,
        name=x._keras_history.layer.name) for x in self.inputs])
