# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(Activation, self).__init__(**kwargs)
self.supports_masking = True
self.activation = activations.get(activation)
