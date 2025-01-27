# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [1, 2, 3, 1]
out_shape = [1, 4, 6, 1]

x = np.arange(0, 6).reshape(in_shape).astype(np.float32)

kernel_types = [
    'lanczos1', 'lanczos3', 'lanczos5', 'gaussian', 'box', 'triangle',
    'keyscubic', 'mitchellcubic'
]
scales = [(1.0, 1.0), (0.37, 0.47), (2.1, 2.1)]
translations = [(0.0, 0.0), (3.14, 1.19), (2.1, 3.1), (100.0, 200.0)]
for scale in scales:
    for translation in translations:
        for kernel_type in kernel_types:
            for antialias in [True, False]:
                with self.cached_session():
                    input_tensor = constant_op.constant(x, shape=in_shape)

                    def scale_trans(input_tensor,
                                    scale=scale,
                                    translation=translation,
                                    kernel_type=kernel_type,
                                    antialias=antialias):
                        # pylint: disable=cell-var-from-loop
                        exit(image_ops.scale_and_translate(
                            input_tensor,
                            out_shape[1:3],
                            scale=constant_op.constant(scale),
                            translation=constant_op.constant(translation),
                            kernel_type=kernel_type,
                            antialias=antialias))

                    err = gradient_checker_v2.max_error(
                        *gradient_checker_v2.compute_gradient(scale_trans,
                                                              [input_tensor]))

                self.assertLess(err, 1e-3)
