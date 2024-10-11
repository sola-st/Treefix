# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
del restored_shapes  # Unused.
self.obj.a.assign(restored_tensors[0])
self.obj.b.assign(restored_tensors[1])
