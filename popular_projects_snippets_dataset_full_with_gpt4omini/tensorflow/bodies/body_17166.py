# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
y = image_ops.resize_images_v2(image, target_shape, target_method)
if method == image_ops.ResizeMethod.NEAREST_NEIGHBOR:
    expected_dtype = image.dtype
else:
    expected_dtype = dtypes.float32

self.assertEqual(y.dtype, expected_dtype)
