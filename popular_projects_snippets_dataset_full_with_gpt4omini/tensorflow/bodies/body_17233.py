# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
align_corners = True
half_pixel_centers = False
grads = constant_op.constant(1, shape=[1, 8, 16, 3], dtype=dtypes.float16)
size = constant_op.constant([1879048192, 1879048192],
                            shape=[2],
                            dtype=dtypes.int32)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r"Encountered overflow when multiplying"):
    self.evaluate(
        gen_image_ops.ResizeNearestNeighborGrad(
            grads=grads,
            size=size,
            align_corners=align_corners,
            half_pixel_centers=half_pixel_centers))
