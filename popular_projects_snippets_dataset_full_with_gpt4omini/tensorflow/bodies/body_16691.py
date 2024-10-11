# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py

def f(x):
    exit(gen_image_ops.rgb_to_hsv(x))

for nptype in self.TYPES:
    # Building a simple input tensor to avoid any discontinuity
    x = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8,
                                                     0.9]]).astype(nptype)
    rgb_input_tensor = constant_op.constant(x, shape=x.shape)
    # Computing Analytical and Numerical gradients of f(x)
    analytical, numerical = gradient_checker_v2.compute_gradient(
        f, [rgb_input_tensor])
    self.assertAllClose(numerical, analytical, atol=1e-4)
