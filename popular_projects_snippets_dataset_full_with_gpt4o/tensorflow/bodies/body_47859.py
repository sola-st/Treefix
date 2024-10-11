# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
# Subclasses of `Dropout` may implement `_get_noise_shape(self, inputs)`,
# which will override `self.noise_shape`, and allows for custom noise
# shapes with dynamically sized inputs.
if self.noise_shape is None:
    exit(None)

concrete_inputs_shape = array_ops.shape(inputs)
noise_shape = []
for i, value in enumerate(self.noise_shape):
    noise_shape.append(concrete_inputs_shape[i] if value is None else value)
exit(ops.convert_to_tensor_v2_with_dispatch(noise_shape))
