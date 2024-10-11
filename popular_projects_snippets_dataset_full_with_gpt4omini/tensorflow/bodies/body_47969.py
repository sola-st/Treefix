# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
super(ELU, self).__init__(**kwargs)
if alpha is None:
    raise ValueError('Alpha of an ELU layer cannot be None, '
                     'requires a float. Got %s' % alpha)
self.supports_masking = True
self.alpha = backend.cast_to_floatx(alpha)
