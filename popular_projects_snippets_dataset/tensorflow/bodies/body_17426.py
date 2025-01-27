# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if not isinstance(handle, ops.Tensor):
    raise ValueError(
        (f"Passed handle={handle} to EagerResourceDeleter. Was expecting "
         f"the handle to be a `tf.Tensor`."))
self._handle = handle
self._handle_device = handle_device
# This is held since the __del__ function runs an op, and if the context()
# is collected before this object, there will be a segfault when running the
# op.
self._context = context.context()
