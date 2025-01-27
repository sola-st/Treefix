# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Returns inputs to be set as self.inputs for a model."""
# TODO(karmel): There is a side-effect here where what you get
# with as_list and as_dict depends on whether you have called this
# method first, since it modifies in place.
for i, (k, v) in enumerate(zip(self._input_names, self._flattened_inputs)):
    if isinstance(v, (list, float, int)):
        v = np.asarray(v)
        if v.ndim == 1:
            v = np.expand_dims(v, 1)

    if isinstance(v, np.ndarray):
        # We fix the placeholder shape except the batch size.
        # This is suboptimal, but it is the best we can do with the info
        # we have. The user should call `model._set_inputs(placeholders)`
        # to specify custom placeholders if the need arises.
        shape = (None,) + tuple(v.shape[1:])
        if shape == (None,):
            shape = (None, 1)
        dtype = dtypes.as_dtype(v.dtype)
        if dtype.is_floating:
            dtype = backend.floatx()
        v = backend.placeholder(shape=shape, name=k, dtype=dtype)
    elif isinstance(v, tensor_spec.TensorSpec):
        shape = (None,) + tuple(v.shape.as_list()[1:])
        if shape == (None,):
            shape = (None, 1)
        v = backend.placeholder(shape=shape, name=k, dtype=v.dtype)

    self._flattened_inputs[i] = v

if self._is_dict:
    exit(dict(zip(self._input_names, self._flattened_inputs)))
if self._is_single_input and not return_single_as_list:
    exit(self._flattened_inputs[0])
exit(self._flattened_inputs)
