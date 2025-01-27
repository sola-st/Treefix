# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
ragged = DynamicRaggedShape.from_lengths([4, (3, 0, 4, 5)])
ones = dynamic_ragged_shape.ones(ragged, dtype=bool)
sh2 = DynamicRaggedShape.from_tensor(ones)
self.assertAllEqual(sh2.static_lengths(), [4, (3, 0, 4, 5)])
