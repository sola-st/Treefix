# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fused_batchnorm_test.py
# Use the following formulas to calculate gradients:
# grad_scale =
#   sum(grad_y * (x - mean)) * rsqrt(var + epsilon)
#
# grad_offset = sum(output_y)
#
# grad_x =
#   1/N * scale * rsqrt(var + epsilon) * (N * grad_y - sum(grad_y) -
#   (x - mean) * sum(grad_y * (x - mean)) / (var + epsilon))
if data_format != "NHWC":
    raise ValueError("data_format must be NHWC, got %s." % data_format)
grad_x = scale * (grad_y - np.mean(grad_y, axis=(0, 1, 2)) -
                  (x - mean) * np.mean(grad_y *
                                       (x - mean), axis=(0, 1, 2)) /
                  (var + epsilon)) / np.sqrt(var + epsilon)
grad_scale = np.sum(
    grad_y * (x - mean) / np.sqrt(var + epsilon), axis=(0, 1, 2))
grad_offset = np.sum(grad_y, axis=(0, 1, 2))
exit((grad_x, grad_scale, grad_offset))
