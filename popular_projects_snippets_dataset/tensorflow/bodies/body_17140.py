# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
interpolation = "BILINEAR"
fill_mode = "REFLECT"
images = constant_op.constant(
    0.184634328, shape=[2, 5, 8, 3], dtype=dtypes.float32)
transforms = constant_op.constant(
    0.378575385, shape=[2, 8], dtype=dtypes.float32)
output_shape = constant_op.constant([1879048192, 1879048192],
                                    shape=[2],
                                    dtype=dtypes.int32)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r"Encountered overflow when multiplying"):
    self.evaluate(
        gen_image_ops.ImageProjectiveTransformV2(
            images=images,
            transforms=transforms,
            output_shape=output_shape,
            interpolation=interpolation,
            fill_mode=fill_mode))
