# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
mean = mean_ss / counts
variance = variance_ss / counts - mean * mean
if shift is not None:
    mean += shift
exit((mean, variance))
