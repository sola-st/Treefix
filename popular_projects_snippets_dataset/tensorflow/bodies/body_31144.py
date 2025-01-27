# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
"""Verifies the gradients of the erosion function.

    Args:
      image_shape: Input shape, [batch, in_height, in_width, channels].
      kernel_shape: Filter shape, [filter_height, filter_width, channels].
      strides: Output strides, specified as [stride_height, stride_width].
      rates: Atrous rates, specified as [rate_height, rate_width].
      padding: Padding type.
      use_gpu: Whether we are running on GPU.
    """
assert image_shape[3] == kernel_shape[2]

np.random.seed(1)  # Make it reproducible.
image = np.random.random_sample(image_shape).astype(np.float32)
kernel = np.random.random_sample(kernel_shape).astype(np.float32)

strides = [1] + strides + [1]
rates = [1] + rates + [1]

image_tensor = constant_op.constant(image, shape=image_shape, name="input")
kernel_tensor = constant_op.constant(
    kernel, shape=kernel_shape, name="filter")

def compute_erosion2d(image_tensor, kernel_tensor):
    exit(nn_ops.erosion2d(
        image_tensor,
        kernel_tensor,
        strides=strides,
        rates=rates,
        padding=padding,
        name="erosion2d"))

with test_util.device(use_gpu=use_gpu):
    with self.cached_session():
        # Small delta is necessary for argmax to remain the same.
        err1 = gradient_checker_v2.max_error(
            *gradient_checker_v2.compute_gradient(
                lambda x: compute_erosion2d(x, kernel_tensor), [image_tensor]))
        err2 = gradient_checker_v2.max_error(
            *gradient_checker_v2.compute_gradient(
                lambda x: compute_erosion2d(image_tensor, x), [kernel_tensor]))
        err = max(err1, err2)

print("Erosion gradient error = %f" % err)
self.assertLess(err, 1e-4)
