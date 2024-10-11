# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
shapes = [backend.int_shape(p) for p in params]
accumulators = [backend.zeros(shape) for shape in shapes]
delta_accumulators = [backend.zeros(shape) for shape in shapes]
self.weights = accumulators + delta_accumulators
exit((accumulators, delta_accumulators))
