# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Sets attributes related to the inputs of the Model."""
if self.inputs:
    raise ValueError('Model inputs are already set.')

if self.__class__.__name__ == 'Sequential' and not self.built:
    if tensor_util.is_tf_type(inputs):
        input_shape = (None,) + tuple(inputs.shape.as_list()[1:])
    elif isinstance(inputs, tensor_shape.TensorShape):
        input_shape = (None,) + tuple(inputs.as_list()[1:])
    elif isinstance(inputs, dict):
        # We assert that the first layer is a FeatureLayer.
        if not training_utils_v1.is_feature_layer(self.layers[0]):
            raise ValueError('Passing a dictionary input to a Sequential Model '
                             'which doesn\'t have FeatureLayer as the first layer'
                             ' is an error.')
        input_shape = (None,)
    else:
        input_shape = (None,) + tuple(inputs.shape[1:])
    self._build_input_shape = input_shape

# Cast inputs to the compute dtype. This is primarily used
# when saving to determine the correct dtype in the input signature.
inputs = self._maybe_cast_inputs(inputs)

# On-the-fly setting of symbolic model inputs (either by using the tensor
# provided, or by creating a placeholder if Numpy data was provided).
model_inputs = training_utils_v1.ModelInputs(inputs)
inputs = model_inputs.get_symbolic_inputs()
self.inputs = model_inputs.get_symbolic_inputs(return_single_as_list=True)
self.input_names = model_inputs.get_input_names()

self._feed_inputs = []
self._feed_input_names = []
self._feed_input_shapes = []

for k, v in model_inputs.as_dict():
    if backend.is_placeholder(v):
        self._feed_input_names.append(k)
        self._feed_inputs.append(v)
        self._feed_input_shapes.append(backend.int_shape(v))

exit(inputs)
