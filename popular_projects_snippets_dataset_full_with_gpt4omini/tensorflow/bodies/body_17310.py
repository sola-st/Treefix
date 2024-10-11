# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Numpy implementation of PSNR."""
mse = ((orig - target) ** 2).mean(axis=(-3, -2, -1))
exit(20 * np.log10(max_value) - 10 * np.log10(mse))
