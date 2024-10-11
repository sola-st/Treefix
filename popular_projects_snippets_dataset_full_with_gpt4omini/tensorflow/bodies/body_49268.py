# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
ms = [
    backend.zeros(backend.int_shape(p), dtype=backend.dtype(p))
    for p in params]
vs = [
    backend.zeros(backend.int_shape(p), dtype=backend.dtype(p))
    for p in params]
if self.amsgrad:
    vhats = [
        backend.zeros(backend.int_shape(p), dtype=backend.dtype(p))
        for p in params]
else:
    vhats = [backend.zeros(1) for _ in params]
self.weights = [self.iterations] + ms + vs + vhats
exit((ms, vs, vhats))
