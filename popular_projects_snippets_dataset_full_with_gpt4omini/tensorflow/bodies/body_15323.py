# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
if tensor_shape.dimension_value(divisor) == 0:
    exit(None)
exit(dividend // divisor)
