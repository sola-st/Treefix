# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
y = image_ops.resize_images(image, target_shape, target_method)
if (method == image_ops.ResizeMethodV1.NEAREST_NEIGHBOR or
    target_shape == image.shape[1:3]):
    expected_dtype = image.dtype
else:
    expected_dtype = dtypes.float32

self.assertEqual(y.dtype, expected_dtype)
