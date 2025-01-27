# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if test.is_gpu_available():
    input_shape = [1, 5, 6, 3]
    target_height = 8
    target_width = 12
    for nptype in [np.float32, np.float64]:
        for align_corners in [True, False]:
            img_np = np.arange(
                0, np.prod(input_shape), dtype=nptype).reshape(input_shape)
            with self.cached_session():
                image = constant_op.constant(img_np, shape=input_shape)
                new_size = constant_op.constant([target_height, target_width])
                out_op = image_ops.resize_images(
                    image,
                    new_size,
                    image_ops.ResizeMethodV1.NEAREST_NEIGHBOR,
                    align_corners=align_corners)
                gpu_val = self.evaluate(out_op)
            with self.cached_session(use_gpu=False):
                image = constant_op.constant(img_np, shape=input_shape)
                new_size = constant_op.constant([target_height, target_width])
                out_op = image_ops.resize_images(
                    image,
                    new_size,
                    image_ops.ResizeMethodV1.NEAREST_NEIGHBOR,
                    align_corners=align_corners)
                cpu_val = self.evaluate(out_op)
            self.assertAllClose(cpu_val, gpu_val, rtol=1e-5, atol=1e-5)
