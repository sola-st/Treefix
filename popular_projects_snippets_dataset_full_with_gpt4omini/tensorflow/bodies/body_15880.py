# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
rt = ragged_factory_ops.constant([[[1, 2], [3]], [[4]]])
original = DynamicRaggedShape.from_tensor(rt)
actual = original._merge_dims(0, 1)
self.assertAllEqual(actual[0], 3)
