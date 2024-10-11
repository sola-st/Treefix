# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
if scale <= 0.:
    raise ValueError('`scale` must be positive float.')
if mode not in {'fan_in', 'fan_out', 'fan_avg'}:
    raise ValueError('Invalid `mode` argument:', mode)
distribution = distribution.lower()
# Compatibility with keras-team/keras.
if distribution == 'normal':
    distribution = 'truncated_normal'
if distribution not in {'uniform', 'truncated_normal',
                        'untruncated_normal'}:
    raise ValueError('Invalid `distribution` argument:', distribution)
self.scale = scale
self.mode = mode
self.distribution = distribution
self.seed = seed
self._random_generator = _RandomGenerator(seed)
