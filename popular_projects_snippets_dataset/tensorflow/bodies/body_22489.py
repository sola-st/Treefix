# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
del restored_shapes  # unused
exit(self.restore_function(
    *[restored_tensors[i] for i in range(len(self.specs))]))
