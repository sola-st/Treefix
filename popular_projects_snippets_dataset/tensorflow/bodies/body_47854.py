# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
exit(K.any(math_ops.not_equal(inputs, self.mask_value), axis=-1))
