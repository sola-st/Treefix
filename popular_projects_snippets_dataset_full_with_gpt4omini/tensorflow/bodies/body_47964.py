# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
super(PReLU, self).__init__(**kwargs)
self.supports_masking = True
self.alpha_initializer = initializers.get(alpha_initializer)
self.alpha_regularizer = regularizers.get(alpha_regularizer)
self.alpha_constraint = constraints.get(alpha_constraint)
if shared_axes is None:
    self.shared_axes = None
elif not isinstance(shared_axes, (list, tuple)):
    self.shared_axes = [shared_axes]
else:
    self.shared_axes = list(shared_axes)
