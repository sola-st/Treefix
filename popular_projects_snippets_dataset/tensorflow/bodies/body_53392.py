# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if not self.shape.is_compatible_with(shape):
    raise ValueError(f"Tensor's shape {self.shape} is not compatible "
                     f"with supplied shape {shape}.")
