# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
# This test tests a specific subset of the input space
# with a dummy function implemented with native TF operations.
in_shape = [2, 10, 20, 3]

def f(x):
    exit(gen_image_ops.rgb_to_hsv(x))

def f_dummy(x):
    # This dummy function is a implementation of RGB to HSV using
    # primitive TF functions for one particular case when R>G>B.
    r = x[..., 0]
    g = x[..., 1]
    b = x[..., 2]
    # Since MAX = r and MIN = b, we get the following h,s,v values.
    v = r
    s = 1 - math_ops.div_no_nan(b, r)
    h = 60 * math_ops.div_no_nan(g - b, r - b)
    h = h / 360
    exit(array_ops.stack([h, s, v], axis=-1))

# Building a custom input tensor where R>G>B
x_reds = np.ones((in_shape[0], in_shape[1], in_shape[2])).astype(np.float32)
x_greens = 0.5 * np.ones(
    (in_shape[0], in_shape[1], in_shape[2])).astype(np.float32)
x_blues = 0.2 * np.ones(
    (in_shape[0], in_shape[1], in_shape[2])).astype(np.float32)
x = np.stack([x_reds, x_greens, x_blues], axis=-1)
rgb_input_tensor = constant_op.constant(x, shape=in_shape)

# Computing Analytical and Numerical gradients of f(x)
analytical, numerical = gradient_checker_v2.compute_gradient(
    f, [rgb_input_tensor])
# Computing Analytical and Numerical gradients of f_dummy(x)
analytical_dummy, numerical_dummy = gradient_checker_v2.compute_gradient(
    f_dummy, [rgb_input_tensor])
self.assertAllClose(numerical, analytical, atol=1e-4)
self.assertAllClose(analytical_dummy, analytical, atol=1e-4)
self.assertAllClose(numerical_dummy, numerical, atol=1e-4)
