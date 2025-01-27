# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape inference in V1.
with ops.Graph().as_default():
    target_shapes = [[6, 4], [3, 2], [
        array_ops.placeholder(dtypes.int32),
        array_ops.placeholder(dtypes.int32)
    ]]
    for nptype in self.TYPES:
        image = array_ops.placeholder(nptype, shape=[1, 6, 4, 1])
        for method in self.METHODS:
            for target_shape in target_shapes:
                y = image_ops.resize_images(image, target_shape, method)
                if (method == image_ops.ResizeMethodV1.NEAREST_NEIGHBOR or
                    target_shape == image.shape[1:3]):
                    expected_dtype = image.dtype
                else:
                    expected_dtype = dtypes.float32
                self.assertEqual(y.dtype, expected_dtype)
