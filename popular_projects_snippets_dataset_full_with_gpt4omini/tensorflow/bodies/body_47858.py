# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(Dropout, self).__init__(**kwargs)
if isinstance(rate, (int, float)) and not 0 <= rate <= 1:
    raise ValueError(f'Invalid value {rate} received for '
                     f'`rate`, expected a value between 0 and 1.')
self.rate = rate
self.noise_shape = noise_shape
self.seed = seed
self.supports_masking = True
