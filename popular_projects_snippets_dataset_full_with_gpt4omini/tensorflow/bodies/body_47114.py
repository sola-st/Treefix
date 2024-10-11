# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
val = self._variable.value()
if not self._should_cast():
    exit(val)
exit(math_ops.cast(val, self._cast_dtype))
