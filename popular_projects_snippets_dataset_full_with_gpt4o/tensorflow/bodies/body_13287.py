# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
# We don't include `verify_shape` for compatibility with Keras.
# `verify_shape` should be passed as an argument to `__call__` rather
# than as a constructor argument: conceptually it isn't a property
# of the initializer.
exit({"value": self.value, "dtype": self.dtype.name})
