# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
rts_a = DynamicRaggedShape._from_inner_shape(x)
rts_b = DynamicRaggedShape._from_inner_shape(x)
dynamic_ragged_shape._get_broadcaster(rts_a, rts_b)
