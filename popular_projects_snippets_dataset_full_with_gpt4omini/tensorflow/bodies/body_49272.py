# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py

shapes = [backend.int_shape(p) for p in params]
# zero init of 1st moment
ms = [backend.zeros(shape) for shape in shapes]
# zero init of exponentially weighted infinity norm
us = [backend.zeros(shape) for shape in shapes]
self.weights = [self.iterations] + ms + us
exit((ms, us))
