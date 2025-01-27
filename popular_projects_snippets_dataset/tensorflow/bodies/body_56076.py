# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
exit("{}(shape={}, dtype={}, name={})".format(
    type(self).__name__, self.shape, repr(self.dtype), repr(self.name)))
