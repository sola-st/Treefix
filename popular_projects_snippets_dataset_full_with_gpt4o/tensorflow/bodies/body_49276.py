# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
shapes = [backend.int_shape(p) for p in params]
ms = [backend.zeros(shape) for shape in shapes]
vs = [backend.zeros(shape) for shape in shapes]

self.weights = [self.iterations, self.m_schedule] + ms + vs
exit((ms, vs))
