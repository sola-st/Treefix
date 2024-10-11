# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
if factor == 1.0:
    exit(new_val)
else:
    exit((1.0 - factor) * old_mean + factor * new_val)
