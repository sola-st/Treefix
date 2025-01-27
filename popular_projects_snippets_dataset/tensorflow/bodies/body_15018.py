# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
# Sneak the dynamic_size and infer_shape values into the legacy shape.
exit((tensor_shape.TensorShape([self._dynamic_size, self._infer_shape
                                 ]).concatenate(self._element_shape)))
