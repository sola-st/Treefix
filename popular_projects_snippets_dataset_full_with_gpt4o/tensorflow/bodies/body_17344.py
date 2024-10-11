# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# [2 x 4] image but missing batch and depth dimensions.
img = constant_op.constant([[1, 3, 4, 2], [8, 7, 5, 6]])
with self.assertRaises(ValueError):
    image_ops.image_gradients(img)
