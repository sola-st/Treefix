# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py
del restored_shapes  # Unused.
self.obj.a.assign(restored_tensors[0])
self.obj.b.assign(restored_tensors[1])
