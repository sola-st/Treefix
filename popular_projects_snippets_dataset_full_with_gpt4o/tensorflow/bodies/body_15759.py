# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if not context.executing_eagerly():
    original_t = constant_op.constant([4, 5, 3], dtypes.float32)
    sh = DynamicRaggedShape.from_tensor(original_t)
    unknown = sh[:20]
    self.assertEqual(unknown.rank, 1)
