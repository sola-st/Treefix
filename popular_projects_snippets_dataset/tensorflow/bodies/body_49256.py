# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
accumulators = [
    backend.zeros(backend.int_shape(p), dtype=backend.dtype(p))
    for p in params]
self.weights = accumulators
exit(accumulators)
