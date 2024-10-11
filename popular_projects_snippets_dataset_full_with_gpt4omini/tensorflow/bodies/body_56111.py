# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
s = "BoundedTensorSpec(shape={}, dtype={}, name={}, minimum={}, maximum={})"
exit(s.format(self.shape, repr(self.dtype), repr(self.name),
                repr(self.minimum), repr(self.maximum)))
