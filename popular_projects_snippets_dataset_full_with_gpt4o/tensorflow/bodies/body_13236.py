# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
y = (x - m) / np.sqrt(v + epsilon)
y = y * gamma if scale_after_normalization else y
exit(y + beta if shift_after_normalization else y)
