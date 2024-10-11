# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_norm_benchmark.py
"""Python implementation of batch normalization."""
exit(nn_impl.batch_normalization(tensor, mean, variance, beta, gamma if
                                   scale else None, 0.001))
