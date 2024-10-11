# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
exit(TensorSpec(
    tensor_shape.TensorShape([batch_size]).concatenate(self._shape),
    self._dtype))
