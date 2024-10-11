# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
# This step does not need to be pipelined because NumPy empty array
# initialization is effectively instantaneous.
shape = (self.num_samples,) + batch_element.shape[1:]
dtype = batch_element.dtype

self.results = np.empty(shape=shape, dtype=dtype)
