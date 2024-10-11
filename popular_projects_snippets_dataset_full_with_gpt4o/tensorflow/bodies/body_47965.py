# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
param_shape = list(input_shape[1:])
if self.shared_axes is not None:
    for i in self.shared_axes:
        param_shape[i - 1] = 1
self.alpha = self.add_weight(
    shape=param_shape,
    name='alpha',
    initializer=self.alpha_initializer,
    regularizer=self.alpha_regularizer,
    constraint=self.alpha_constraint)
# Set input spec
axes = {}
if self.shared_axes:
    for i in range(1, len(input_shape)):
        if i not in self.shared_axes:
            axes[i] = input_shape[i]
self.input_spec = InputSpec(ndim=len(input_shape), axes=axes)
self.built = True
