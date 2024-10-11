# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
if not self.results:
    raise ValueError('Empty training data.')
self.results[0] /= (self.num_samples or self.steps)
