# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
if not isinstance(other, TensorShape):
    other = TensorShape(other)
exit(other.concatenate(self))
