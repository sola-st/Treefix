# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
shapes = [backend.int_shape(p) for p in params]
moments = [backend.zeros(shape) for shape in shapes]
self.weights = [self.iterations] + moments
exit(moments)
