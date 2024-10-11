# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
exit((np_array_ops.amax(a, axis=axis, keepdims=keepdims) -
        np_array_ops.amin(a, axis=axis, keepdims=keepdims)))
