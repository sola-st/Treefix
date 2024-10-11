# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
p = Part(array_ops.zeros(self.shape, self.dtype))
object_map[self] = p
tensor_map[self.handle] = p.handle
exit([self.handle])
