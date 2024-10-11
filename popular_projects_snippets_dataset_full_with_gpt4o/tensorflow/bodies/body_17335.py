# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
exit(image_ops.ssim_multiscale(
    x1 * scalar,
    x2 * scalar,
    max_val=1.0,
    power_factors=(1, 1, 1, 1, 1),
    filter_size=11,
    filter_sigma=1.5,
    k1=0.01,
    k2=0.03))
