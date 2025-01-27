# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if not context.executing_eagerly():
    original_t = array_ops.placeholder_with_default(np.array([4, 5, 3]), None)
    sh = DynamicRaggedShape.from_tensor(original_t)
    unknown = sh[:20]
    self.assertIsNone(unknown.rank)
