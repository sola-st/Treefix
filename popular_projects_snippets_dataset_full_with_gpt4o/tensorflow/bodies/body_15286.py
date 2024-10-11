# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
# Assumes a_0 == 1
a_layer = math_ops.range(a_0)
b_layer = math_ops.range(b_0)
target = b
exit([a_layer, b_layer, target])
