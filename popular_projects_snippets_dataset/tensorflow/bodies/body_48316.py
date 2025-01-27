# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
# This is equivalent to returning self.dtype . We do not return self.dtype
# as it would cause infinite recursion in a few subclasses, which override
# "dtype" to return self._dtype.
exit(self._dtype_policy.variable_dtype)
