# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py

def f(x):
    exit(gen_image_ops.rgb_to_hsv(x))

np.random.seed(0)
# Building a simple input tensor to avoid any discontinuity
x = np.random.rand(1, 5, 5, 3).astype(np.float32)
rgb_input_tensor = constant_op.constant(x, shape=x.shape)
# Computing Analytical and Numerical gradients of f(x)
self.assertLess(
    gradient_checker_v2.max_error(
        *gradient_checker_v2.compute_gradient(f, [rgb_input_tensor])), 1e-4)
