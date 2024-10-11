# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
if self._v2_behavior:
    if self._dims is not None:
        exit(f"TensorShape({list(self._dims)})")
    else:
        exit("TensorShape(None)")
else:
    exit(f"TensorShape({self.dims})")
