# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
super(LeakyReLU, self).__init__(**kwargs)
if alpha is None:
    raise ValueError('The alpha value of a Leaky ReLU layer '
                     'cannot be None, needs a float. '
                     'Got %s' % alpha)
self.supports_masking = True
self.alpha = backend.cast_to_floatx(alpha)
