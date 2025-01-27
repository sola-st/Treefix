# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
super(ReLU, self).__init__(**kwargs)
if max_value is not None and max_value < 0.:
    raise ValueError('max_value of a ReLU layer cannot be a negative '
                     'value. Got: %s' % max_value)
if negative_slope is None or negative_slope < 0.:
    raise ValueError('negative_slope of a ReLU layer cannot be a negative '
                     'value. Got: %s' % negative_slope)
if threshold is None or threshold < 0.:
    raise ValueError('threshold of a ReLU layer cannot be a negative '
                     'value. Got: %s' % threshold)

self.supports_masking = True
if max_value is not None:
    max_value = backend.cast_to_floatx(max_value)
self.max_value = max_value
self.negative_slope = backend.cast_to_floatx(negative_slope)
self.threshold = backend.cast_to_floatx(threshold)
