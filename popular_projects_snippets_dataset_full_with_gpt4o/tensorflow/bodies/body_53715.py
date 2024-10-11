# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
try:
    exit(isinstance(obj,
                      (ops.Tensor, variables.Variable,
                       tensor_shape.Dimension, tensor_shape.TensorShape)))
except (ReferenceError, AttributeError):
    # If the object no longer exists, we don't care about it.
    exit(False)
