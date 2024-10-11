# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
self.minval = minval
self.maxval = maxval
self.seed = seed
self._random_generator = _RandomGenerator(seed)
