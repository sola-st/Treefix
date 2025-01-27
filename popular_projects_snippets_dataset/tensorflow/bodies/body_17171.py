# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 3, 2, 1]
data = [64, 32, 32, 64, 50, 100]
target_height = 6
target_width = 4
methods_to_test = ((gen_image_ops.resize_bilinear, "triangle"),
                   (gen_image_ops.resize_bicubic, "keyscubic"))
for legacy_method, new_method in methods_to_test:
    with self.cached_session():
        img_np = np.array(data, dtype=np.float32).reshape(img_shape)
        image = constant_op.constant(img_np, shape=img_shape)
        legacy_result = legacy_method(
            image,
            constant_op.constant([target_height, target_width],
                                 dtype=dtypes.int32),
            half_pixel_centers=True)
        scale = (
            constant_op.constant([target_height, target_width],
                                 dtype=dtypes.float32) /
            math_ops.cast(array_ops.shape(image)[1:3], dtype=dtypes.float32))
        new_result = gen_image_ops.scale_and_translate(
            image,
            constant_op.constant([target_height, target_width],
                                 dtype=dtypes.int32),
            scale,
            array_ops.zeros([2]),
            kernel_type=new_method,
            antialias=False)
        self.assertAllClose(
            self.evaluate(legacy_result), self.evaluate(new_result), atol=1e-04)
