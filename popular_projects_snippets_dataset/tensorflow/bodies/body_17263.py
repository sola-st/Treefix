# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session():
    image = constant_op.constant(
        np.arange(24, dtype=np.uint8).reshape([2, 4, 3]))
    adjusted_image = image_ops.adjust_jpeg_quality(image, 80)
    adjusted_image.shape.assert_is_compatible_with([None, None, 3])
