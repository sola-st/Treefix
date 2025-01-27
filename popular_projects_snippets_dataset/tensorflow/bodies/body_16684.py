# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
"""Tests that Gradients for 1.0 scale should be ones for some kernels."""
in_shape = [1, 2, 3, 1]
out_shape = [1, 4, 6, 1]

x = np.arange(0, 6).reshape(in_shape).astype(np.float32)

kernel_types = ['lanczos1', 'lanczos3', 'lanczos5', 'triangle', 'keyscubic']
scale = (1.0, 1.0)
translation = (0.0, 0.0)
antialias = True
for kernel_type in kernel_types:
    with self.cached_session():
        input_tensor = constant_op.constant(x, shape=in_shape)
        with backprop.GradientTape() as tape:
            tape.watch(input_tensor)
            scale_and_translate_out = image_ops.scale_and_translate(
                input_tensor,
                out_shape[1:3],
                scale=constant_op.constant(scale),
                translation=constant_op.constant(translation),
                kernel_type=kernel_type,
                antialias=antialias)
        grad = tape.gradient(scale_and_translate_out, input_tensor)[0]
        grad_v = self.evaluate(grad)
        self.assertAllClose(np.ones_like(grad_v), grad_v)
