# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if test.is_gpu_available():
    input_shape = [1, 5, 6, 3]
    target_height = 8
    target_width = 12
    for nptype in [np.float32, np.float64]:
        img_np = np.arange(
            0, np.prod(input_shape), dtype=nptype).reshape(input_shape)
        value = {}
        for use_gpu in [True, False]:
            with self.cached_session(use_gpu=use_gpu):
                image = constant_op.constant(img_np, shape=input_shape)
                new_size = constant_op.constant([target_height, target_width])
                out_op = image_ops.resize_images(image, new_size,
                                                 image_ops.ResizeMethod.BILINEAR)
                value[use_gpu] = self.evaluate(out_op)
        self.assertAllClose(value[True], value[False], rtol=1e-5, atol=1e-5)
