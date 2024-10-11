# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape._from_inner_shape(x)
b = DynamicRaggedShape._from_inner_shape([1, 1, 1])
dynamic_ragged_shape.broadcast_dynamic_shape_extended(a, b)
