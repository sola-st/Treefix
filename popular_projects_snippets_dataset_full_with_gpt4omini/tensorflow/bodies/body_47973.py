# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
super(ThresholdedReLU, self).__init__(**kwargs)
if theta is None:
    raise ValueError('Theta of a Thresholded ReLU layer cannot be '
                     'None, requires a float. Got %s' % theta)
if theta < 0:
    raise ValueError('The theta value of a Thresholded ReLU layer '
                     'should be >=0, got %s' % theta)
self.supports_masking = True
self.theta = backend.cast_to_floatx(theta)
